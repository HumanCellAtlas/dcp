#!/usr/bin/env python3

import os
import re
import unittest

from ..utils import Progress, Timeout
from ..data_store_agent import DataStoreAgent
from ..dataset_fixture import DatasetFixture
from ..dataset_runner import DatasetRunner

DEPLOYMENTS = ('dev', 'staging', 'integration', 'prod')


class TestEndToEndDCP(unittest.TestCase):

    def setUp(self):
        self.deployment = os.environ.get('CI_COMMIT_REF_NAME', None)
        if self.deployment not in DEPLOYMENTS:
            raise RuntimeError(f"CI_COMMIT_REF_NAME environment variable must be one of {DEPLOYMENTS}")
        self.data_store = DataStoreAgent(deployment=self.deployment)

    def ingest_store_and_analyze_dataset(self, runner, dataset_fixture):
        dataset = DatasetFixture(dataset_fixture, deployment=self.deployment)
        runner.run(dataset, run_name_prefix=self.deployment)

    def expected_results_bundle_files(self, primary_bundle_uuid, analysis_results_files_regexes):
        primary_bundle_manifest = self.data_store.bundle_manifest(primary_bundle_uuid)
        primary_files_names = (file['name'] for file in primary_bundle_manifest['bundle']['files'])
        primary_files_regexes = (re.compile(f"^{re.escape(filename)}$") for filename in primary_files_names)

        expected_files_regexes = list(primary_files_regexes)
        expected_files_regexes += analysis_results_files_regexes

        # Bundle structure creates file schema for each analysis output file
        result_file_schemas_regexes = [re.compile(f"^analysis_file_{re.escape(str(num))}\.json")
                                          for num in range(len(analysis_results_files_regexes))]

        # Metadata schema requires a new analysis_process between runs
        analysis_process_regex = re.compile(f"^analysis_process_0\.json$")

        # Metadata schema requires a new analysis_protocol which is static between runs unless the pipeline is changed
        analysis_protocol_regex = re.compile(f"^analysis_protocol_0\.json$")

        expected_files_regexes += result_file_schemas_regexes
        expected_files_regexes.append(analysis_process_regex)
        expected_files_regexes.append(analysis_protocol_regex)

        return expected_files_regexes

    def check_manifest_contains_exactly_these_files(self, bundle_manifest, filename_regexes):
        Progress.report("CHECKING RESULTS...\n")
        files = bundle_manifest['bundle']['files']
        for filename_regex in filename_regexes:
            Progress.report(f"Checking for \"{filename_regex.pattern}...\" ")
            try:
                file_index = next(index for (index, file) in enumerate(files) if filename_regex.match(file["name"]))
                Progress.report(f"found {files[file_index]['name']}\n")
                self.assertGreater(files[file_index]['size'], 0)
                del(files[file_index])
            except StopIteration:
                self.fail(f"couldn't find {filename_regex.pattern} in {list((f['name'] for f in files))}")
        self.assertEqual(len(files), 0, f"Found extra file(s) in bundle: {list((f['name'] for f in files))}")


class TestSmartSeq2Run(TestEndToEndDCP):

    SS2_ANALYSIS_OUTPUT_FILES_REGEXES = [
        re.compile('^.+\_qc\.bam$'),  # aligned_bam
        re.compile('^.+\_qc\.bam\.bai$'),  # bam_index
        re.compile('^.+\_qc\.insert\_size\_metrics\.txt$'),  # insert_size_metrics
        re.compile('^.+\_qc\.quality\_distribution\_metrics\.txt$'),  # quality_distribution_metrics
        re.compile('^.+\_qc\.quality\_by\_cycle\_metrics\.txt$'),  # quality_by_cycle_metrics
        re.compile('^.+\_qc\.bait\_bias\_summary\_metrics\.txt$'),  # bait_bias_summary_metrics
        re.compile('^.+\_qc\.rna\_metrics\.txt$'),  # rna_metrics
        re.compile('^.+\_QCs\.csv$'),  # QCs
        re.compile('^.+\_bait\_bias\_detail\_metrics\.csv$'),  # bait_bias_detail_metrics
        re.compile('^.+\_base\_distribution\_by\_cycle\_metrics\.csv$'),  # base_distribution_by_cycle_metrics
        re.compile('^.+\_error\_summary\_metrics\.csv$'),  # error_summary_metrics
        re.compile('^.+\_gc\_bias\.csv$'),  # gc_bias
        re.compile('^.+\_pre\_adapter\_detail\_metrics\.csv$'),  # pre_adapter_detail_metrics
        re.compile('^.+\_pre\_adapter\_summary\_metrics\.csv$'),  # pre_adapter_summary_metrics
        re.compile('^.+\_rsem\.bam$'),  # aligned_trans_bam
        re.compile('^.+\_rsem\.genes\.results$'),  # rsem_gene_results
        re.compile('^.+\_rsem\.isoforms\.results$'),  # rsem_isoform_results
        re.compile('^.+zarr!\.zattrs$'),
        re.compile('^.+zarr!\.zgroup$'),
        re.compile('^.+zarr!cell_id!\.zarray$'),
        re.compile('^.+zarr!cell_id!0$'),
        re.compile('^.+zarr!cell_metadata_numeric_name!\.zarray$'),
        re.compile('^.+zarr!cell_metadata_numeric_name!0$'),
        re.compile('^.+zarr!cell_metadata_numeric!\.zarray$'),
        re.compile('^.+zarr!cell_metadata_numeric!0\.0$'),
        re.compile('^.+zarr!cell_metadata_string_name!\.zarray$'),
        re.compile('^.+zarr!cell_metadata_string_name!0$'),
        re.compile('^.+zarr!cell_metadata_string!\.zarray$'),
        re.compile('^.+zarr!cell_metadata_string!0\.0$'),
        re.compile('^.+zarr!expression!\.zarray$'),
        re.compile('^.+zarr!expression!0\.0$'),
        re.compile('^.+zarr!gene_id!\.zarray$'),
        re.compile('^.+zarr!gene_id!0$'),
    ]

    def test_smartseq2_run(self):
        runner = DatasetRunner(deployment=self.deployment)

        with Timeout(110 * 60) as to:  # timeout after 1 hour and 50 minutes
            try:
                self.ingest_store_and_analyze_dataset(runner, dataset_fixture='Smart-seq2')
                self.assertEqual(1, len(runner.primary_bundle_uuids))
                self.assertEqual(1, len(runner.secondary_bundle_uuids))
                expected_files = self.expected_results_bundle_files(runner.primary_bundle_uuids[0],
                                                                    self.SS2_ANALYSIS_OUTPUT_FILES_REGEXES)
                results_bundle_manifest = self.data_store.bundle_manifest(runner.secondary_bundle_uuids[0])
    
                self.check_manifest_contains_exactly_these_files(results_bundle_manifest, expected_files)
            finally:
                runner.cleanup_primary_and_result_bundles()
                runner.cleanup_analysis_workflows()

        if to.did_timeout:
            raise TimeoutError("test timed out")


class TestOptimusRun(TestEndToEndDCP):

    OPTIMUS_10X_ANALYSIS_OUTPUT_FILES_REGEXES = [
        re.compile('merged\.bam$'),
        re.compile('sparse\_counts\.npz$'),
        re.compile('sparse\_counts\_row\_index\.npy$'),
        re.compile('sparse\_counts\_col\_index\.npy$'),
        re.compile('merged-cell-metrics\.csv\.gz$'),
        re.compile('merged-gene-metrics\.csv\.gz$'),
        re.compile('empty\_drops\_result\.csv$'),
        re.compile('^.+zarr!\.zattrs$'),
        re.compile('^.+zarr!\.zgroup$'),
        re.compile('^.+zarr!expression_matrix!\.zgroup$'),
        re.compile('^.+zarr!expression_matrix!cell_id!\.zarray$'),
        re.compile('^.+zarr!expression_matrix!cell_id!0$'),
        re.compile('^.+zarr!expression_matrix!cell_id!1$'),
        re.compile('^.+zarr!expression_matrix!cell_metadata_numeric!\.zarray$'),
        re.compile('^.+zarr!expression_matrix!cell_metadata_numeric!0\.0$'),
        re.compile('^.+zarr!expression_matrix!cell_metadata_numeric_name!\.zarray$'),
        re.compile('^.+zarr!expression_matrix!cell_metadata_numeric_name!0$'),
        re.compile('^.+zarr!expression_matrix!expression!\.zarray$'),
        re.compile('^.+zarr!expression_matrix!expression!0\.0$'),
        re.compile('^.+zarr!expression_matrix!expression!0\.1$'),
        re.compile('^.+zarr!expression_matrix!expression!0\.2$'),
        re.compile('^.+zarr!expression_matrix!expression!0\.3$'),
        re.compile('^.+zarr!expression_matrix!expression!0\.4$'),
        re.compile('^.+zarr!expression_matrix!expression!0\.5$'),
        re.compile('^.+zarr!expression_matrix!expression!1\.0$'),
        re.compile('^.+zarr!expression_matrix!expression!1\.1$'),
        re.compile('^.+zarr!expression_matrix!expression!1\.2$'),
        re.compile('^.+zarr!expression_matrix!expression!1\.3$'),
        re.compile('^.+zarr!expression_matrix!expression!1\.4$'),
        re.compile('^.+zarr!expression_matrix!expression!1\.5$'),
        re.compile('^.+zarr!expression_matrix!gene_id!\.zarray$'),
        re.compile('^.+zarr!expression_matrix!gene_id!0$'),
        re.compile('^.+zarr!expression_matrix!gene_id!1$'),
        re.compile('^.+zarr!expression_matrix!gene_id!2$'),
        re.compile('^.+zarr!expression_matrix!gene_id!3$'),
        re.compile('^.+zarr!expression_matrix!gene_id!4$'),
        re.compile('^.+zarr!expression_matrix!gene_id!5$'),
        re.compile('^.+zarr!expression_matrix!gene_metadata_numeric!\.zarray$'),
        re.compile('^.+zarr!expression_matrix!gene_metadata_numeric!0\.0$'),
        re.compile('^.+zarr!expression_matrix!gene_metadata_numeric_name!\.zarray$'),
        re.compile('^.+zarr!expression_matrix!gene_metadata_numeric_name!0$')
    ]

    def test_optimus_run(self):
        runner = DatasetRunner(deployment=self.deployment)

        with Timeout(210 * 60) as to:  # timeout after 3.5 hours (same as Gitlab runner setting)
            try:
                self.ingest_store_and_analyze_dataset(runner, dataset_fixture='optimus')
                self.assertEqual(1, len(runner.primary_bundle_uuids))
                self.assertEqual(1, len(runner.secondary_bundle_uuids))
                expected_files = self.expected_results_bundle_files(runner.primary_bundle_uuids[0],
                                                                    self.OPTIMUS_10X_ANALYSIS_OUTPUT_FILES_REGEXES)
                results_bundle_manifest = self.data_store.bundle_manifest(runner.secondary_bundle_uuids[0])

                self.check_manifest_contains_exactly_these_files(results_bundle_manifest, expected_files)
            finally:
                runner.cleanup_primary_and_result_bundles()
                runner.cleanup_analysis_workflows()

        if to.did_timeout:
            raise TimeoutError("test timed out")


if __name__ == '__main__':
    unittest.main()

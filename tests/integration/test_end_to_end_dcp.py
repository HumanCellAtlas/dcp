#!/usr/bin/env python3

import os
import re
import unittest

from ..utils import Progress
from ..data_store_agent import DataStoreAgent
from ..dataset_fixture import DatasetFixture
from ..dataset_runner import DatasetRunner

DEPLOYMENTS = ('dev', 'staging', 'integration', 'prod')


class TestEndToEndDCP(unittest.TestCase):

    def setUp(self):
        self.deployment = os.environ.get('TRAVIS_BRANCH', None)
        if self.deployment not in DEPLOYMENTS:
            raise RuntimeError(f"TRAVIS_BRANCH environment variable must be one of {DEPLOYMENTS}")
        self.data_store = DataStoreAgent(deployment=self.deployment)

    def ingest_store_and_analyze_dataset(self, dataset_fixture):
        dataset = DatasetFixture(dataset_fixture)
        runner = DatasetRunner(deployment=self.deployment)
        runner.run(dataset)
        return runner

    def expected_results_bundle_files(self, primary_bundle_uuid, analysis_results_files_regexes):
        primary_bundle_manifest = self.data_store.bundle_manifest(primary_bundle_uuid)
        primary_files_names = (file['name'] for file in primary_bundle_manifest['bundle']['files'])
        primary_files_regexes = (re.compile(f"^{re.escape(filename)}$") for filename in primary_files_names)

        expected_files_regexes = list(primary_files_regexes)
        expected_files_regexes += analysis_results_files_regexes
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
        re.compile('^.+\_qc\.alignment\_summary\_metrics\.txt$'),  # alignment_summary_metrics
        re.compile('^.+\_qc\.bait\_bias\_detail\_metrics\.txt$'),  # bait_bias_detail_metrics
        re.compile('^.+\_qc\.bait\_bias\_summary\_metrics\.txt$'),  # bait_bias_summary_metrics
        re.compile('^.+\_qc\.base\_distribution\_by\_cycle\_metrics\.txt$'),  # base_call_dist_metrics
        re.compile('^.+\_qc\.base\_distribution\_by\_cycle\.pdf$'),  # base_call_pdf
        re.compile('^.+\_qc\.duplicate\_metrics\.txt$'),  # dedup_metrics
        re.compile('^.+\_qc\.error\_summary\_metrics\.txt$'),  # error_summary_metrics
        re.compile('^.+\_qc\.gc\_bias\.detail\_metrics\.txt$'),  # gc_bias_detail_metrics
        re.compile('^.+\_qc\.gc\_bias\.pdf$'),  # gc_bias_dist_pdf
        re.compile('^.+\_qc\.gc\_bias\.summary\_metrics\.txt$'),  # gc_bias_summary_metrics
        re.compile('^.+\_qc\.insert\_size\_histogram\.pdf$'),  # insert_size_hist
        re.compile('^.+\_qc\.insert\_size\_metrics\.txt$'),  # insert_size_metrics
        re.compile('^.+\_qc\.log$'),  # hisat2_logfile
        re.compile('^.+\_qc\.hisat2\.met\.txt$'),  # hisat2_metfile
        re.compile('^.+\_qc\.pre\_adapter\_detail\_metrics\.txt$'),  # pre_adapter_details_metrics
        re.compile('^.+\_qc\.quality\_by\_cycle\_metrics\.txt$'),  # quality_by_cycle_metrics
        re.compile('^.+\_qc\.quality\_by\_cycle\.pdf$'),  # quality_by_cycle_pdf
        re.compile('^.+\_qc\.quality\_distribution\.pdf$'),  # quality_distribution_dist_pdf
        re.compile('^.+\_qc\.quality\_distribution\_metrics\.txt$'),  # quality_distribution_metrics
        re.compile('^.+\_qc\.rna\.coverage\.pdf$'),  # rna_coverage
        re.compile('^.+\_qc\.rna\_metrics\.txt$'),  # rna_metrics
        re.compile('^.+\_rsem\.bam$'),  # aligned_trans_bam
        re.compile('^.+\_rsem\.log$'),  # hisat2tran_logfile
        re.compile('^.+\_rsem\.hisat2\.met\.txt$'),  # hisat2tran_metfile
        re.compile('^.+\_rsem\.cnt$'),  # rsem_cnt_log
        re.compile('^.+\_rsem\.genes\.results$'),  # rsem_gene_results
        re.compile('^.+\_rsem\.isoforms\.results$'),  # rsem_isoform_results
        re.compile('^.+\_rsem\.model$'),  # rsem_model_log
        re.compile('^.+\_rsem\.theta$'),  # rsem_theta_log
        re.compile('^.+\_rsem\.time$')  # rsem_time_log
    ]

    def test_smartseq2_run(self):
        runner = self.ingest_store_and_analyze_dataset(dataset_fixture='Smart-seq2')
        expected_files = self.expected_results_bundle_files(runner.primary_bundle_uuid,
                                                            self.SS2_ANALYSIS_OUTPUT_FILES_REGEXES)
        results_bundle_manifest = self.data_store.bundle_manifest(runner.secondary_bundle_uuid)

        self.check_manifest_contains_exactly_these_files(results_bundle_manifest, expected_files)


if __name__ == '__main__':
    unittest.main()

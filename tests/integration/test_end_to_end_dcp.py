#!/usr/bin/env python3

import os
import re
import unittest

import openpyxl
import requests

from ingest.importer.submission import Submission

from tests.wait_for import WaitFor
from ..utils import Progress, Timeout
from ..cloudwatch_handler import CloudwatchHandler
from ..data_store_agent import DataStoreAgent
from ..dataset_fixture import DatasetFixture
from ..dataset_runner import DatasetRunner

cloudwatch_handler = CloudwatchHandler()
DEPLOYMENTS = ('dev', 'staging', 'integration', 'prod')


class TestEndToEndDCP(unittest.TestCase):

    def setUp(self):
        self.deployment = os.environ.get('DEPLOYMENT_ENV', None)
        if self.deployment not in DEPLOYMENTS:
            raise RuntimeError(f"DEPLOYMENT_ENV environment variable must be one of {DEPLOYMENTS}")
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
        self._run_end_to_end_test_template(post_condition=self._assert_bundle_creation_succeeded)

    def _assert_bundle_creation_succeeded(self, runner, *args, **kwargs):
        self.assertEqual(1, len(runner.primary_bundle_uuids))
        self.assertEqual(1, len(runner.secondary_bundle_uuids))
        expected_files = self.expected_results_bundle_files(runner.primary_bundle_uuids[0],
                                                            self.SS2_ANALYSIS_OUTPUT_FILES_REGEXES)
        results_bundle_manifest = self.data_store.bundle_manifest(runner.secondary_bundle_uuids[0])
        self.check_manifest_contains_exactly_these_files(results_bundle_manifest, expected_files)

    def test_update(self):
        self._run_end_to_end_test_template(post_condition=self._run_update_test)

    def _run_update_test(self, runner, *args, **kwargs):
        # given:
        original_submission = runner.submission_envelope

        # when:
        update_submission = self._do_update_submission(runner, original_submission)
        Progress.report(f"UPDATE submission ID is {update_submission.envelope_id}\n")
        Progress.report('Checking validation status of update submission...')
        WaitFor(update_submission.check_validation).to_return_value(True)

        # then:
        update_bundle_uuids = self._complete_submission(update_submission)
        Progress.report(f'Bundle UUIDs {update_bundle_uuids}.')

        self.analysis_agent = runner.analysis_agent
        self.primary_bundle = runner.primary_bundle_uuids[0]
        self.analysis_workflow_set = set([])
        self.expected_update_workflow_count = 1
        self._wait_for_analysis_workflows()

    def _do_update_submission(self, runner, original_submission):
        update_spreadsheet_content = runner.ingest_broker.download(original_submission.uuid)
        update_spreadsheet_filename = f'{original_submission.uuid}.xlsx'
        update_spreadsheet_path = os.path.abspath(os.path.join(os.path.dirname(__file__), update_spreadsheet_filename))
        with open(update_spreadsheet_path, 'wb') as f:
            f.write(update_spreadsheet_content)

        update_spreadsheet = openpyxl.load_workbook(update_spreadsheet_path)
        project_worksheet = update_spreadsheet['Project']
        if project_worksheet['B4'].value != "project.project_core.project_short_name":
            raise RuntimeError("Project shortname is no longer in cell project!B4")
        project_worksheet['B6'] = f"UPDATED {project_worksheet['B6'].value}"

        update_spreadsheet.save(update_spreadsheet_path)

        update_submission_id = runner.ingest_broker.upload(update_spreadsheet_path, is_update=True)
        update_submission = runner.ingest_api.submission(update_submission_id)

        return update_submission

    @staticmethod
    def _complete_submission(update_submission):
        Progress.report('Completing update submission...')
        update_submission.complete()
        WaitFor(update_submission.bundles).to_return_any_value()
        update_bundle_uuids = update_submission.bundles()
        Progress.report(f'Updated bundles {update_bundle_uuids}')
        return update_bundle_uuids

    def _wait_for_analysis_workflows(self):
        if not self.analysis_agent:
            Progress.report("NO CREDENTIALS PROVIDED FOR ANALYSIS AGENT, SKIPPING WORKFLOW(s) CHECK...")
        else:
            Progress.report("WAITING FOR UPDATED ANALYSIS WORKFLOW(s) TO ABORT...")
            WaitFor(
                self._count_aborted_analysis_workflows_and_report
            ).to_return_value(value=self.expected_update_workflow_count)

    def _count_aborted_analysis_workflows_and_report(self):
        if self._aborted_analysis_workflows_count() < self.expected_update_workflow_count:
            self._count_analysis_workflows()
        Progress.report("  aborted analysis workflows: {}/{}".format(
            self._aborted_analysis_workflows_count(),
            self.expected_update_workflow_count
        ))
        return self._aborted_analysis_workflows_count()

    def _count_analysis_workflows(self):
        with self.analysis_agent.ignore_logging_msg():
            try:
                workflows = self.analysis_agent.query_by_bundle(self.primary_bundle)
                self.analysis_workflow_set.update(workflows)
            except requests.exceptions.HTTPError:
                pass

    def _aborted_analysis_workflows_count(self):
        return len(
            list(filter(lambda wf: wf.status in ('Aborting', 'Aborted'), self.analysis_workflow_set))
        )

    def _run_end_to_end_test_template(self, test_runner=None, post_condition=None):
        cloudwatch_handler.put_metric_data('dcp-ss2-test-invocation', 1)
        runner = test_runner if test_runner else DatasetRunner(deployment=self.deployment)
        _1_hr_50_min = 110 * 60
        with Timeout(_1_hr_50_min) as time_limit:
            try:
                self.ingest_store_and_analyze_dataset(runner, dataset_fixture='Smart-seq2')
                if post_condition:
                    post_condition(runner)
            except:
                cloudwatch_handler.put_metric_data('dcp-ss2-test-failure', 1)
                raise
            finally:
                runner.cleanup_primary_and_result_bundles()

        if time_limit.did_timeout:
            runner.cleanup_analysis_workflows()
            cloudwatch_handler.put_metric_data('dcp-ss2-test-failure', 1)
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
        re.compile('^.+zarr!cell_id!\.zarray$'),
        re.compile('^.+zarr!cell_id!0$'),
        re.compile('^.+zarr!cell_id!1$'),
        re.compile('^.+zarr!cell_metadata_bool!\.zarray$'),
        re.compile('^.+zarr!cell_metadata_bool!0\.0$'),
        re.compile('^.+zarr!cell_metadata_bool_name!\.zarray$'),
        re.compile('^.+zarr!cell_metadata_bool_name!0$'),
        re.compile('^.+zarr!cell_metadata_float!\.zarray$'),
        re.compile('^.+zarr!cell_metadata_float!0\.0$'),
        re.compile('^.+zarr!cell_metadata_float!0\.1$'),
        re.compile('^.+zarr!cell_metadata_float!1\.0$'),
        re.compile('^.+zarr!cell_metadata_float!1\.1$'),
        re.compile('^.+zarr!cell_metadata_float_name!\.zarray$'),
        re.compile('^.+zarr!cell_metadata_float_name!0$'),
        re.compile('^.+zarr!expression!\.zarray$'),
        re.compile('^.+zarr!expression!0\.0$'),
        re.compile('^.+zarr!expression!0\.1$'),
        re.compile('^.+zarr!expression!0\.2$'),
        re.compile('^.+zarr!expression!0\.3$'),
        re.compile('^.+zarr!expression!0\.4$'),
        re.compile('^.+zarr!expression!0\.5$'),
        re.compile('^.+zarr!expression!1\.0$'),
        re.compile('^.+zarr!expression!1\.1$'),
        re.compile('^.+zarr!expression!1\.2$'),
        re.compile('^.+zarr!expression!1\.3$'),
        re.compile('^.+zarr!expression!1\.4$'),
        re.compile('^.+zarr!expression!1\.5$'),
        re.compile('^.+zarr!gene_id!\.zarray$'),
        re.compile('^.+zarr!gene_id!0$'),
        re.compile('^.+zarr!gene_id!1$'),
        re.compile('^.+zarr!gene_id!2$'),
        re.compile('^.+zarr!gene_id!3$'),
        re.compile('^.+zarr!gene_id!4$'),
        re.compile('^.+zarr!gene_id!5$'),
        re.compile('^.+zarr!gene_metadata_numeric!\.zarray$'),
        re.compile('^.+zarr!gene_metadata_numeric!0\.0$'),
        re.compile('^.+zarr!gene_metadata_numeric_name!\.zarray$'),
        re.compile('^.+zarr!gene_metadata_numeric_name!0$'),
        re.compile('^.+zarr!gene_metadata_string!\.zarray$'),
        re.compile('^.+zarr!gene_metadata_string!0\.0$'),
        re.compile('^.+zarr!gene_metadata_string_name!\.zarray$'),
        re.compile('^.+zarr!gene_metadata_string_name!0$'),
    ]

    def test_optimus_run(self):
        cloudwatch_handler.put_metric_data('dcp-optimus-test-invocation', 1)
        runner = DatasetRunner(deployment=self.deployment)
        with Timeout(240 * 60) as to:  # timeout after 4hrs (less than the Gitlab runner setting) to allow for test cleanup
            try:
                self.ingest_store_and_analyze_dataset(runner, dataset_fixture='optimus')
                self.assertEqual(1, len(runner.primary_bundle_uuids))
                self.assertEqual(1, len(runner.secondary_bundle_uuids))
                expected_files = self.expected_results_bundle_files(runner.primary_bundle_uuids[0],
                                                                    self.OPTIMUS_10X_ANALYSIS_OUTPUT_FILES_REGEXES)
                results_bundle_manifest = self.data_store.bundle_manifest(runner.secondary_bundle_uuids[0])

                self.check_manifest_contains_exactly_these_files(results_bundle_manifest, expected_files)
            except:
                cloudwatch_handler.put_metric_data('dcp-optimus-test-failure', 1)
                raise
            finally:
                runner.cleanup_primary_and_result_bundles()

        if to.did_timeout:
            runner.cleanup_analysis_workflows()
            cloudwatch_handler.put_metric_data('dcp-optimus-test-failure', 1)
            raise TimeoutError("test timed out")


if __name__ == '__main__':
    unittest.main()

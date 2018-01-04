#!/usr/bin/env python3

import os
import re
import subprocess
import unittest

import requests

from .utils import Progress
from .wait_for import WaitFor
from .ingest_agents import IngestUIAgent, IngestApiAgent
from .data_store_agent import DataStoreAgent
from .bundle_fixture import BundleFixture

DEPLOYMENTS = ('dev', 'staging', 'prod')


class BundleRunner:

    def __init__(self, deployment):
        self.ingest_broker = IngestUIAgent(deployment=deployment)
        self.ingest_api = IngestApiAgent(deployment=deployment)
        self.data_store = DataStoreAgent(deployment=deployment)
        self.submission_id = None
        self.submission_envelope = None
        self.upload_credentials = None
        self.primary_bundle_uuid = None
        self.secondary_bundle_uuid = None

    def run(self, bundle):
        self.upload_spreadsheet_and_create_submission(bundle)
        self.get_upload_area_credentials()
        self.stage_data_files(bundle)
        self.forget_about_upload_area()
        self.wait_for_envelope_to_be_validated()
        self.complete_submission()
        self.wait_for_bundle_to_be_created()
        self.wait_for_results_bundle_to_be_created()
        return self.secondary_bundle_uuid

    def upload_spreadsheet_and_create_submission(self, bundle):
        Progress.report("CREATING SUBMISSION...")
        self.submission_id = self.ingest_broker.upload(bundle.metadata_spreadsheet_path())
        Progress.report(f" submission ID is {self.submission_id}\n")
        self.submission_envelope = self.ingest_api.envelope(self.submission_id)

    def get_upload_area_credentials(self):
        Progress.report("WAITING FOR STAGING AREA...")
        self.upload_credentials = WaitFor(
            self._get_upload_area_credentials
        ).to_return_a_value_other_than(other_than_value=None, timeout_seconds=60)
        Progress.report(" credentials received.\n")

    def _get_upload_area_credentials(self):
        return self.submission_envelope.reload().upload_credentials()

    def stage_data_files(self, bundle):
        Progress.report("STAGING FILES...\n")
        self._run_command(['hca', 'upload', 'select', self.upload_credentials])
        for file_path in bundle.data_files_paths():
            self._run_command(['hca', 'upload', 'file', file_path])

    def forget_about_upload_area(self):
        upload_area_uuid = self.upload_credentials.split(':')[4]
        self._run_command(['hca', 'upload', 'forget', upload_area_uuid])

    def wait_for_envelope_to_be_validated(self):
        Progress.report("WAIT FOR VALIDATION...")
        WaitFor(self._envelope_is_valid).to_return_value(value=True, timeout_seconds=5 * 60)
        Progress.report(" envelope is valid.\n")

    def _envelope_is_valid(self):
        return self.submission_envelope.reload().status() in ['Valid', 'Submitted']

    def complete_submission(self):
        Progress.report("COMPLETING SUBMISSION...")
        submit_url = self.submission_envelope.data['_links']['submit']['href']
        response = requests.put(submit_url, headers=self.ingest_api.auth_headers)
        if response.status_code != requests.codes.accepted:
            raise RuntimeError(f"PUT {submit_url} returned {response.status_code}: {response.content}")
        Progress.report(" done.\n")

    def wait_for_bundle_to_be_created(self):
        Progress.report("WAITING FOR PRIMARY BUNDLE UUID...")
        bundles = WaitFor(
            self.submission_envelope.bundles
        ).to_return_a_value_other_than(other_than_value=[], timeout_seconds=5*60)
        assert len(bundles) == 1
        self.primary_bundle_uuid = bundles[0]
        Progress.report(f" {self.primary_bundle_uuid}\n")

    def wait_for_results_bundle_to_be_created(self):
        Progress.report("WAIT FOR RESULTS BUNDLE...")
        secondary_bundle_id = WaitFor(
            self._results_bundle
        ).to_return_a_value_other_than(other_than_value=None, timeout_seconds=90*60)
        Progress.report(f" {secondary_bundle_id}\n")
        self.secondary_bundle_uuid = secondary_bundle_id.split('.')[0]

    def _results_bundle(self):
        results = self.data_store.search(
            {
                "query": {
                    "match": {
                        "files.analysis_json.content.input_bundles": self.primary_bundle_uuid
                    }
                }
            }
        )
        if len(results) == 1:
            # "bundle_id": "61f2f401-de4b-4918-89bc-7cfd7f381c6e.2017-11-15T182943.100876Z"
            return results[0]['bundle_id'].split('.')[0]
        else:
            return None

    @staticmethod
    def _run_command(cmd_and_args_list, expected_retcode=0):
        retcode = subprocess.call(cmd_and_args_list)
        if retcode != 0:
            raise Exception(
                "Unexpected return code from '{command}', expected {expected_retcode} got {actual_retcode}".format(
                    command=" ".join(cmd_and_args_list), expected_retcode=expected_retcode, actual_retcode=retcode
                )
            )


class TestEndToEndDCP(unittest.TestCase):

    def setUp(self):
        self.deployment = os.environ.get('TRAVIS_BRANCH', None)
        if self.deployment not in DEPLOYMENTS:
            raise RuntimeError(f"TRAVIS_BRANCH environment variable must be one of {DEPLOYMENTS}")
        self.data_store = DataStoreAgent(deployment=self.deployment)

    def ingest_store_and_analyze_bundle(self, bundle_fixture_path):
        bundle_fixture = BundleFixture(bundle_fixture_path)
        runner = BundleRunner(deployment=self.deployment)
        runner.run(bundle_fixture)
        return runner

    def expected_results_bundle_files(self, primary_bundle_uuid, analysis_results_files_regexes):
        primary_bundle_manifest = self.data_store.bundle_manifest(primary_bundle_uuid)
        primary_files_names = (file['name'] for file in primary_bundle_manifest['bundle']['files'])
        primary_files_regexes = (re.compile(f"^{re.escape(filename)}$") for filename in primary_files_names)

        expected_files_regexes = list(primary_files_regexes)
        expected_files_regexes += analysis_results_files_regexes
        expected_files_regexes.append(re.compile('^analysis\.json$'))
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

    SMARTSEQ2_BUNDLE_FIXTURE_PATH = 'tests/fixtures/bundles/Smart-seq2'
    SS2_ANALYSIS_OUTPUT_FILES_REGEXES = [
        re.compile('^Aligned\.sortedByCoord\.out\.bam$'),
        re.compile('^Aligned\.toTranscriptome\.out\.bam$'),
        re.compile('^.+_rna_metrics$'),
        re.compile('^.+_alignment_metrics$'),
        re.compile('^.+\.genes\.results$'),
        re.compile('^.+\.isoforms\.results$'),
        re.compile('^.+\.gene\.expected_counts$'),
        re.compile('^.+\.gene\.counts\.txt$'),
        re.compile('^.+\.exon\.counts\.txt$'),
        re.compile('^.+\.transcripts\.counts\.txt$')
    ]

    def test_smartseq2_run(self):
        runner = self.ingest_store_and_analyze_bundle(self.SMARTSEQ2_BUNDLE_FIXTURE_PATH)
        expected_files = self.expected_results_bundle_files(runner.primary_bundle_uuid,
                                                            self.SS2_ANALYSIS_OUTPUT_FILES_REGEXES)
        results_bundle_manifest = self.data_store.bundle_manifest(runner.secondary_bundle_uuid)

        self.check_manifest_contains_exactly_these_files(results_bundle_manifest, expected_files)


if __name__ == '__main__':
    unittest.main()

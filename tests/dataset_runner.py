import os
import subprocess

import requests

from .data_store_agent import DataStoreAgent
from .ingest_agents import IngestUIAgent, IngestApiAgent
from .utils import Progress
from .wait_for import WaitFor


class DatasetRunner:

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_broker = IngestUIAgent(deployment=deployment)
        self.ingest_api = IngestApiAgent(deployment=deployment)
        self.data_store = DataStoreAgent(deployment=deployment)
        self.submission_id = None
        self.submission_envelope = None
        self.upload_credentials = None
        self.primary_bundle_uuid = None
        self.secondary_bundle_uuid = None

    def run(self, dataset):
        self.upload_spreadsheet_and_create_submission(dataset)
        self.get_upload_area_credentials()
        self.stage_data_files(dataset)
        self.wait_for_envelope_to_be_validated()
        self.complete_submission()
        self.wait_for_bundle_to_be_created()
        self.wait_for_results_bundle_to_be_created()
        return self.secondary_bundle_uuid

    def upload_spreadsheet_and_create_submission(self, dataset):
        spreadhseet_filename = os.path.basename(dataset.metadata_spreadsheet_path)
        Progress.report(f"CREATING SUBMISSION with {spreadhseet_filename}...")
        self.submission_id = self.ingest_broker.upload(dataset.metadata_spreadsheet_path)
        Progress.report(f"  submission ID is {self.submission_id}\n")
        self.submission_envelope = self.ingest_api.envelope(self.submission_id)

    def get_upload_area_credentials(self):
        Progress.report("WAITING FOR STAGING AREA...")
        self.upload_credentials = WaitFor(
            self._get_upload_area_credentials
        ).to_return_a_value_other_than(other_than_value=None, timeout_seconds=60)
        Progress.report("  credentials received.\n")

    def _get_upload_area_credentials(self):
        return self.submission_envelope.reload().upload_credentials()

    def stage_data_files(self, dataset):
        if dataset.data_files_are_in_s3():
            self._stage_data_files_using_s3_sync(dataset)
        else:
            self._stage_data_files_using_hca_cli(dataset)

    def _stage_data_files_using_hca_cli(self, dataset):
        Progress.report("STAGING FILES using hca cli...")
        self._run_command(['hca', 'upload', 'select', self.upload_credentials])
        for file_path in dataset.data_files_paths():
            self._run_command(['hca', 'upload', 'file', file_path])
        self.forget_about_upload_area()

    def _stage_data_files_using_s3_sync(self, dataset):
        Progress.report("STAGING FILES using aws s3 sync...")
        upload_area_uuid = self.upload_credentials.split(':')[4]
        upload_area_s3_location = f"s3://org-humancellatlas-upload-{self.deployment}/{upload_area_uuid}"
        command = ['aws', 's3', 'sync', '--content-type', 'application/gzip; dcp-type=data',
                   dataset.config['data_files_location'],
                   upload_area_s3_location]
        self._run_command(command)

    def forget_about_upload_area(self):
        upload_area_uuid = self.upload_credentials.split(':')[4]
        self._run_command(['hca', 'upload', 'forget', upload_area_uuid])

    def wait_for_envelope_to_be_validated(self):
        Progress.report("WAIT FOR VALIDATION...")
        WaitFor(self._envelope_is_valid).to_return_value(value=True, timeout_seconds=30 * 60)
        Progress.report(" envelope is valid.\n")

    def _envelope_is_valid(self):
        envelope_status = self.submission_envelope.reload().status()
        Progress.report(f"  envelope status is {envelope_status}")
        return envelope_status in ['Valid', 'Submitted']

    def complete_submission(self):
        Progress.report("COMPLETING SUBMISSION...")
        submit_url = self.submission_envelope.data['_links']['submit']['href']
        response = requests.put(submit_url, headers=self.ingest_api.auth_headers)
        if response.status_code != requests.codes.accepted:
            raise RuntimeError(f"PUT {submit_url} returned {response.status_code}: {response.content}")
        Progress.report("  done.\n")

    def wait_for_bundle_to_be_created(self):
        Progress.report("WAITING FOR PRIMARY BUNDLE UUID...")
        bundles = WaitFor(
            self.submission_envelope.bundles
        ).to_return_a_value_other_than(other_than_value=[], timeout_seconds=5*60)
        assert len(bundles) == 1
        self.primary_bundle_uuid = bundles[0]
        Progress.report(f"  {self.primary_bundle_uuid}\n")

    def wait_for_results_bundle_to_be_created(self):
        Progress.report("WAIT FOR RESULTS BUNDLE...")
        secondary_bundle_id = WaitFor(
            self._results_bundle
        ).to_return_a_value_other_than(other_than_value=None, timeout_seconds=90*60)
        Progress.report(f"  {secondary_bundle_id}\n")
        self.secondary_bundle_uuid = secondary_bundle_id.split('.')[0]

    def _results_bundle(self):
        results = self.data_store.search(
            {
                "query": {
                    "match": {
                        "files.process_json.processes.content.input_bundles": self.primary_bundle_uuid
                    }
                }
            }
        )
        if len(results) == 1:
            # "bundle_id": "61f2f401-de4b-4918-89bc-7cfd7f381c6e.2017-11-15T182943.100876Z"
            # Blue Box has standardized their naming, so "bundle_id" became "bundle_fqid" now.
            # "bundle_fqid": "21597770-bfbd-4b77-9eb8-a20dcbb42cec.2018-01-05T164438.271840Z"
            return results[0]['bundle_fqid'].split('.')[0]
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



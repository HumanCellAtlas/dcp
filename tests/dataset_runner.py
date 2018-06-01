import os
import subprocess

import requests

from .data_store_agent import DataStoreAgent
from .ingest_agents import IngestUIAgent, IngestApiAgent
from .utils import Progress
from .wait_for import WaitFor, TimedOut

MINUTE = 60


class DatasetRunner:

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_broker = IngestUIAgent(deployment=deployment)
        self.ingest_api = IngestApiAgent(deployment=deployment)
        self.data_store = DataStoreAgent(deployment=deployment)
        self.dataset = None
        self.submission_id = None
        self.submission_envelope = None
        self.upload_credentials = None
        self.primary_to_results_bundles_map = {}
        self.failure_reason = None

    @property
    def primary_bundle_uuids(self):
        return list(self.primary_to_results_bundles_map.keys())

    @property
    def secondary_bundle_uuids(self):
        return list(self.primary_to_results_bundles_map.values())

    def run(self, dataset_fixture):
        self.dataset = dataset_fixture
        self.upload_spreadsheet_and_create_submission()
        self.wait_for_ingest_to_process_spreadsheet_files_tab()
        self.get_upload_area_credentials()
        self.stage_data_files()
        self.wait_for_envelope_to_be_validated()
        self.complete_submission()
        self.wait_for_primary_bundles_to_be_created()
        self.wait_for_results_bundle_to_be_created()
        if self.failure_reason:
            raise RuntimeError(self.failure_reason)

    def upload_spreadsheet_and_create_submission(self):
        spreadsheet_filename = os.path.basename(self.dataset.metadata_spreadsheet_path)
        Progress.report(f"CREATING SUBMISSION with {spreadsheet_filename}...")
        self.submission_id = self.ingest_broker.upload(self.dataset.metadata_spreadsheet_path)
        Progress.report(f"  submission ID is {self.submission_id}\n")
        self.submission_envelope = self.ingest_api.submission(self.submission_id)

    def wait_for_ingest_to_process_spreadsheet_files_tab(self):
        file_count = self._how_many_files_do_we_expect()
        Progress.report(f"WAIT FOR INGEST TO PROCESS {file_count} SPREADSHEET FILE ROWS...")
        self.upload_credentials = WaitFor(
            self._submission_files_count
        ).to_return_value(value=file_count)

    def _how_many_files_do_we_expect(self):
        return self.dataset.count_of_rows_in_spreadsheet_tab('sequence_file')

    def _submission_files_count(self):
        return len(self.submission_envelope.reload().files())

    def get_upload_area_credentials(self):
        Progress.report("WAITING FOR STAGING AREA...")
        self.upload_credentials = WaitFor(
            self._get_upload_area_credentials
        ).to_return_a_value_other_than(other_than_value=None, timeout_seconds=2 * MINUTE)
        Progress.report("  credentials received.\n")

    def _get_upload_area_credentials(self):
        return self.submission_envelope.reload().upload_credentials()

    def stage_data_files(self):
        if self.dataset.data_files_are_in_s3():
            self._stage_data_files_using_s3_sync()
        else:
            self._stage_data_files_using_hca_cli()

    def _stage_data_files_using_hca_cli(self):
        Progress.report("STAGING FILES using hca cli...")
        self._run_command(['hca', 'upload', 'select', self.upload_credentials])
        for file_path in self.dataset.data_files_paths():
            self._run_command(['hca', 'upload', 'file', file_path])
        self.forget_about_upload_area()

    def _stage_data_files_using_s3_sync(self):
        Progress.report("STAGING FILES using aws s3 sync...")
        upload_area_uuid = self.upload_credentials.split(':')[4]
        upload_area_s3_location = f"s3://org-humancellatlas-upload-{self.deployment}/{upload_area_uuid}"
        command = ['aws', 's3', 'sync', '--content-type', 'application/gzip; dcp-type=data',
                   self.dataset.config['data_files_location'],
                   upload_area_s3_location]
        self._run_command(command)

    def forget_about_upload_area(self):
        upload_area_uuid = self.upload_credentials.split(':')[4]
        self._run_command(['hca', 'upload', 'forget', upload_area_uuid])

    def wait_for_envelope_to_be_validated(self):
        Progress.report("WAIT FOR VALIDATION...")
        WaitFor(self._envelope_is_valid).to_return_value(value=True)
        Progress.report("  envelope is valid.\n")

    def _envelope_is_valid(self):
        envelope_status = self.submission_envelope.reload().status
        Progress.report(f"  envelope status is {envelope_status}")
        return envelope_status in ['Valid', 'Submitted']

    def complete_submission(self):
        Progress.report("COMPLETING SUBMISSION...")
        submit_url = self.submission_envelope.data['_links']['submit']['href']
        response = requests.put(submit_url, headers=self.ingest_api.auth_headers)
        if response.status_code != requests.codes.accepted:
            raise RuntimeError(f"PUT {submit_url} returned {response.status_code}: {response.content}")
        Progress.report("  done.\n")

    def wait_for_primary_bundles_to_be_created(self):
        Progress.report("WAITING FOR PRIMARY BUNDLE(s) TO BE CREATED...")
        expected_primary_bundle_count = self._how_many_primary_bundles_do_we_expect()
        Progress.report(f"  expecting {expected_primary_bundle_count} primary bundles")
        try:
            WaitFor(
                self._primary_bundle_count
            ).to_return_value(value=expected_primary_bundle_count)
        except TimedOut:
            Progress.report("  We did not get all the primary bundles we expected, "
                            "but let us continue and see how many results bundles we get.")
            self.failure_reason = f"Only received {self._primary_bundle_count()} " \
                                  f"of {expected_primary_bundle_count} primary bundles"
        bundle_uuids = self.submission_envelope.bundles()

        Progress.report(f"  {bundle_uuids}\n")
        for bundle_uuid in bundle_uuids:
            self.primary_to_results_bundles_map[bundle_uuid] = None

    def wait_for_results_bundle_to_be_created(self):
        Progress.report("WAIT FOR RESULTS BUNDLE(s)...")
        Progress.report(f"  waiting for {len(self.primary_to_results_bundles_map)} secondary bundles")
        WaitFor(
            self._results_bundles_count
        ).to_return_value(value=len(self.primary_to_results_bundles_map))
        Progress.report(f"  done.\n")

    def _how_many_primary_bundles_do_we_expect(self):
        """
        Count how many rows there are in the sequencing_process sheet of the spreadsheet.
        This will be the number of bundles created.
        """
        return self.dataset.count_of_rows_in_spreadsheet_tab('sequencing_process')

    def _primary_bundle_count(self):
        return len(self.submission_envelope.bundles())

    def _results_bundles_count(self):
        self._search_for_results_bundles()
        return len(list(v for v in self.primary_to_results_bundles_map.values() if v))

    def _search_for_results_bundles(self):
        for primary_bundle_uuid in self.primary_to_results_bundles_map.keys():
            query = {
                "query": {
                    "match": {
                        "files.process_json.processes.content.input_bundles": primary_bundle_uuid
                        }
                    }
                }
            results = self.data_store.search(query)
            if len(results) > 0:
                results_bundle_uuid = results[0]['bundle_fqid'].split('.')[0]
                self.primary_to_results_bundles_map[primary_bundle_uuid] = results_bundle_uuid

    @staticmethod
    def _run_command(cmd_and_args_list, expected_retcode=0):
        retcode = subprocess.call(cmd_and_args_list)
        if retcode != 0:
            raise Exception(
                "Unexpected return code from '{command}', expected {expected_retcode} got {actual_retcode}".format(
                    command=" ".join(cmd_and_args_list), expected_retcode=expected_retcode, actual_retcode=retcode
                )
            )



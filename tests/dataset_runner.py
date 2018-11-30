import os
import requests
import subprocess

from typing import Set
from urllib.parse import urlparse
from datetime import datetime

from .azul_agent import AzulAgent
from .data_store_agent import DataStoreAgent
from .ingest_agents import IngestUIAgent, IngestApiAgent
from .matrix_agent import MatrixAgent
from .utils import Progress
from .wait_for import WaitFor

MINUTE = 60


class DatasetRunner:

    FASTQ_CONTENT_TYPE = 'application/gzip; dcp-type=data'

    def __init__(self, deployment, export_bundles=True):
        self.deployment = deployment
        self.export_bundles = export_bundles
        self.ingest_broker = IngestUIAgent(deployment=deployment)
        self.ingest_api = IngestApiAgent(deployment=deployment)
        self.data_store = DataStoreAgent(deployment=deployment)
        self.azul_agent = AzulAgent(deployment=deployment)
        self.matrix_agent = MatrixAgent(deployment=deployment)
        self.dataset = None
        self.project_shortname = None
        self.submission_id = None
        self.submission_envelope = None
        self.upload_credentials = None
        self.upload_area_uuid = None
        self.expected_bundle_count = None
        self.primary_uuid_to_secondary_bundle_fqid_map = {}
        self.failure_reason = None

    @property
    def primary_bundle_uuids(self):
        return list(self.primary_uuid_to_secondary_bundle_fqid_map.keys())

    @property
    def secondary_bundle_uuids(self):
        return [fqid.split('.')[0] for fqid in self.primary_uuid_to_secondary_bundle_fqid_map.values()]

    @property
    def secondary_bundle_fqids(self):
        return list(self.primary_uuid_to_secondary_bundle_fqid_map.values())

    def run(self, dataset_fixture, run_name_prefix="test"):
        self.dataset = dataset_fixture
        self.set_project_shortname(run_name_prefix)
        self.upload_spreadsheet_and_create_submission()
        self.wait_for_ingest_to_process_spreadsheet_files_tab()
        self.get_upload_area_credentials()
        self.stage_data_files()
        self.wait_for_envelope_to_be_validated()
        if self.export_bundles:
            self.complete_submission()
            self.wait_for_primary_and_results_bundles()
            if self.dataset.name == "Smart-seq2":
                self.retrieve_zarr_output_from_matrix_service()
                self.retrieve_loom_output_from_matrix_service()
            self.assert_data_browser_bundles()
        if self.failure_reason:
            raise RuntimeError(self.failure_reason)

    def set_project_shortname(self, run_name_prefix):
        self.project_shortname = "{prefix}/{dataset}/{when}".format(
            prefix=run_name_prefix,
            dataset=self.dataset.name,
            when=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'))
        Progress.report(f"UPDATING SPREADSHEET PROJECT SHORTNAME TO {self.project_shortname}")
        self.dataset.update_spreadsheet_project_shortname(self.project_shortname)

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
        return self.dataset.count_of_rows_in_spreadsheet_tab('Sequence file')

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
        self.upload_area_uuid = urlparse(self.upload_credentials).path.split('/')[1]
        self._stage_data_files_using_s3_sync()

    def _stage_data_files_using_s3_sync(self):
        Progress.report("STAGING FILES using aws s3 sync...")
        upload_area_s3_location = f"s3://org-humancellatlas-upload-{self.deployment}/{self.upload_area_uuid}"
        command = ['aws', 's3', 'sync', '--content-type', self.FASTQ_CONTENT_TYPE,
                   self.dataset.config['data_files_location'],
                   upload_area_s3_location]
        self._run_command(command)
        self._band_aid_to_fix_wrong_content_types()

    def _band_aid_to_fix_wrong_content_types(self):
        """
        BAND AID:
        AWS S3 sync fails to set content-type sometimes.
        Examine all the files in the upload area, and for the ones with an incorrect content type,
        re-copy them over themselves with the correct content-type.
        """
        Progress.report("FIXING UPLOADED FILE CONTENT-TYPEs...")
        import boto3
        s3r = boto3.resource('s3')
        bucket = s3r.Bucket(f"org-humancellatlas-upload-{self.deployment}")
        for object_summary in bucket.objects.filter(Prefix=self.upload_area_uuid):
            obj = bucket.Object(object_summary.key)
            if obj.content_type != self.FASTQ_CONTENT_TYPE:
                Progress.report(f"  fixing {obj.key}")
                obj.copy_from(CopySource={'Bucket': bucket.name, 'Key': obj.key},
                              MetadataDirective="REPLACE",
                              ContentType=self.FASTQ_CONTENT_TYPE)

    def forget_about_upload_area(self):
        self._run_command(['hca', 'upload', 'forget', self.upload_area_uuid])

    def wait_for_envelope_to_be_validated(self):
        Progress.report("WAIT FOR VALIDATION...")
        WaitFor(self._envelope_is_valid).to_return_value(value=True)
        Progress.report("  envelope is valid.\n")

    def _envelope_is_valid(self):
        envelope_status = self.submission_envelope.reload().status
        Progress.report(f"  envelope status is {envelope_status}")
        if envelope_status == 'Invalid':
            raise Exception("envelope status is Invalid")
        return envelope_status in ['Valid', 'Submitted']

    def complete_submission(self):
        Progress.report("COMPLETING SUBMISSION...")
        submit_url = self.submission_envelope.data['_links']['submit']['href']
        response = requests.put(submit_url, headers=self.ingest_api.auth_headers)
        if response.status_code != requests.codes.accepted:
            raise RuntimeError(f"PUT {submit_url} returned {response.status_code}: {response.content}")
        Progress.report("  done.\n")

    def wait_for_primary_and_results_bundles(self):
        """
        We used to wait for all primary bundles to be created before starting to look for results.
        It appears that with large submissions, results can start to appear before bundle export is finished,
        so we now monitor both kinds of bundles simultaneously.
        """
        Progress.report("WAITING FOR PRIMARY AND RESULTS BUNDLE(s) TO BE CREATED...")
        self.expected_bundle_count = self.dataset.config["expected_bundle_count"]
        WaitFor(
            self._count_primary_and_secondary_bundles
        ).to_return_value(value=self.expected_bundle_count)

    def _count_primary_and_secondary_bundles(self):
        if self._primary_bundle_count() < self.expected_bundle_count:
            self._count_primary_bundles()
        if self._results_bundles_count() < self.expected_bundle_count:
            self._count_results_bundles()
        Progress.report("  bundles: primary: {}/{}, results: {}/{}".format(
            self._primary_bundle_count(),
            self.expected_bundle_count,
            self._results_bundles_count(),
            self._primary_bundle_count()
        ))
        return self._results_bundles_count()

    def _count_primary_bundles(self):
        for bundle_uuid in self.submission_envelope.bundles():
            if bundle_uuid not in self.primary_uuid_to_secondary_bundle_fqid_map:
                Progress.report(f"    found new primary bundle: {bundle_uuid}")
                self.primary_uuid_to_secondary_bundle_fqid_map[bundle_uuid] = None

    def _primary_bundle_count(self):
        self._count_primary_bundles()
        return len(self.primary_uuid_to_secondary_bundle_fqid_map)

    def _results_bundles_count(self):
        return len(list(v for v in self.primary_uuid_to_secondary_bundle_fqid_map.values() if v))

    def _count_results_bundles(self):
        for primary_bundle_uuid, secondary_bundle_fqid in self.primary_uuid_to_secondary_bundle_fqid_map.items():
            if secondary_bundle_fqid is None:
                query = {
                    "query": {
                        "match": {
                            "files.analysis_process_json.input_bundles": primary_bundle_uuid
                            }
                        }
                    }
                results = self.data_store.search(query)
                if len(results) > 0:
                    results_bundle_fqid = results[0]['bundle_fqid']
                    if self.primary_uuid_to_secondary_bundle_fqid_map[primary_bundle_uuid] is None:
                        Progress.report(f"    found new results bundle: {results_bundle_fqid}")
                        self.primary_uuid_to_secondary_bundle_fqid_map[primary_bundle_uuid] = results_bundle_fqid

    @staticmethod
    def _run_command(cmd_and_args_list, expected_retcode=0):
        retcode = subprocess.call(cmd_and_args_list)
        if retcode != 0:
            raise Exception(
                "Unexpected return code from '{command}', expected {expected_retcode} got {actual_retcode}".format(
                    command=" ".join(cmd_and_args_list), expected_retcode=expected_retcode, actual_retcode=retcode
                )
            )

    def assert_data_browser_bundles(self):
        Progress.report(f"Project shortname: {self.project_shortname}")
        WaitFor(
            self._assert_data_browser_bundles, self.project_shortname
        ).to_return_value(value=True)

    def _assert_data_browser_bundles(self, project_shortname):
        try:
            expected_bundle_uuids = set(self.primary_bundle_uuids).union(self.secondary_bundle_uuids)
            files = self.azul_agent.get_files_py_project(project_shortname)
            bundle_uuids = {bundle['bundleUuid'] for file in files for bundle in file['bundles']}
            assert bundle_uuids == expected_bundle_uuids
            project_shortnames = {project_short_name for file in files for project in file['projects']
                                  for project_short_name in project['projectShortname']}
            assert project_shortnames == {project_shortname}
        except AssertionError as e:
            Progress.report(f"Exception occurred: {e}")
            return False
        else:
            Progress.report(f"{len(bundle_uuids)}/{len(expected_bundle_uuids)}")
            return True

    def retrieve_zarr_output_from_matrix_service(self):
        request_id = self.matrix_agent.post_matrix_request(self.secondary_bundle_fqids)
        WaitFor(
            self.matrix_agent.get_matrix_request, request_id
        ).to_return_value(value="Complete")

    def retrieve_loom_output_from_matrix_service(self):
        request_id = self.matrix_agent.post_matrix_request(self.secondary_bundle_fqids, "loom")
        WaitFor(
            self.matrix_agent.get_matrix_request, request_id
        ).to_return_value(value="Complete")

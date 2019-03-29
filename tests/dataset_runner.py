import os
import json
import requests
import subprocess

from urllib.parse import urlparse
from datetime import datetime
import boto3

from .azul_agent import AzulAgent
from .data_store_agent import DataStoreAgent
from .ingest_agents import IngestUIAgent, IngestApiAgent
from .analysis_agent import AnalysisAgent
from .matrix_agent import MatrixAgent
from .utils import Progress
from .wait_for import WaitFor

MINUTE = 60


class DatasetRunner:

    FASTQ_CONTENT_TYPE = 'application/gzip; dcp-type=data'

    def __init__(self, deployment, export_bundles=True):
        self.s3_client = boto3.client('s3')
        self.deployment = deployment
        self.export_bundles = export_bundles
        self.ingest_broker = IngestUIAgent(deployment=deployment)
        self.ingest_api = IngestApiAgent(deployment=deployment)
        self.data_store = DataStoreAgent(deployment=deployment)
        self.analysis_agent = None
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
        self.analysis_workflow_set = set([])

        gcp_credentials_file_for_analysis = os.environ.get('GCP_ACCOUNT_ANALYSIS_INFO')
        if gcp_credentials_file_for_analysis:
            self.analysis_agent = AnalysisAgent(deployment=deployment, 
                                                service_account_key=json.loads(gcp_credentials_file_for_analysis))

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
        """The entrypoint for running the tests.
        
        Note: we use different logic for scaling tests (tests that with a prefix of "scale") and 
        non-scaling tests (e.g. integration test) during the polling process, to save money and 
        resources. 

        1. If it's in the scaling test mode, once the bundles get exported, the runner will poll
        the following info altogether:
            - primary bundles count
            - ongoing analysis workflows count
            - successful analysis workflows count
            - secondary bundles count
        so the progress in DSS and Analysis is tracked simultaneously
        and single workflow failure won't interfere the test
        
        2. If the test is not a scaling test, we'd like to poll the following info step by step:
            - primary bundles count
            - analysis workflows (name, id, status)
            - secondary bundles count
        so if any of the steps failed, the test will fail early instead of timing out.
        """
        self.dataset = dataset_fixture
        self.set_project_shortname(run_name_prefix)
        self.upload_spreadsheet_and_create_submission()
        self.wait_for_ingest_to_process_spreadsheet_files_tab()
        self.get_upload_area_credentials()
        self.stage_data_files()
        self.wait_for_envelope_to_be_validated()
        if self.export_bundles:
            self.complete_submission()
            if run_name_prefix == "scale":
                # == Scaling Logic ==
                self.wait_for_primary_bundles_analysis_workflows_and_results_bundles()
            else:
                # == Non-scaling Logic ==
                self.wait_for_primary_bundles()
                self.wait_for_analysis_workflows()
                self.wait_for_secondary_bundles()
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
        Progress.report("STAGING FILES using hca cli...")
        self.select_upload_area()
        self.upload_files()
        self.forget_about_upload_area()

    def select_upload_area(self):
        upload_area_s3_location = f"s3://org-humancellatlas-upload-{self.deployment}/{self.upload_area_uuid}/"
        self._run_command(['hca', 'upload', 'select', upload_area_s3_location])

    def upload_files(self):
        self._run_command(['hca', 'upload', 'files', self.dataset.config['data_files_location']])

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
        headers = self.ingest_api.ingest_auth_agent.make_auth_header()
        response = requests.put(submit_url, headers=headers)
        if response.status_code != requests.codes.accepted:
            raise RuntimeError(f"PUT {submit_url} returned {response.status_code}: {response.content}")
        Progress.report("  done.\n")
    
    def wait_for_primary_bundles_analysis_workflows_and_results_bundles(self):
        """
        We wait for all primary bundles to be created before starting to look for results in non-scaling tests.
        It appears that with large submissions, results can start to appear before bundle export is finished,
        so we monitor both kinds of bundles simultaneously in scaling tests.
        """
        Progress.report("WAITING FOR PRIMARY BUNDLE(s), ANALYSIS WORKFLOWS AND RESULTS BUNDLE(s)...")
        self.expected_bundle_count = self.dataset.config["expected_bundle_count"]
        WaitFor(
            self._count_primary_bundles_analysis_workflows_and_results_bundles
        ).to_return_value(value=self.expected_bundle_count)

    def _count_primary_bundles_analysis_workflows_and_results_bundles(self):
        if self._primary_bundle_count() < self.expected_bundle_count:
            self._count_primary_bundles()
        if self._analysis_workflows_count() < self.expected_bundle_count:
            self._batch_count_analysis_workflows_by_project_shortname()
        if self._results_bundles_count() < self.expected_bundle_count:
            self._count_results_bundles()
        Progress.report("  primary bundles: {0}/{1} \n  workflows: running: {2}/{3}, \
                        succeeded: {4}/{5}, failed: {6}/{7} \n   results bundles: {8}/{9} ".format(
            self._primary_bundle_count(),
            self.expected_bundle_count,
            self._ongoing_analysis_workflows_count(),
            self._primary_bundle_count(),
            self._successful_analysis_workflows_count(),
            self._primary_bundle_count(),
            self._failed_analysis_workflows_count(),
            self._primary_bundle_count(),
            self._results_bundles_count(),
            self._primary_bundle_count()
        ))
        return self._results_bundles_count()

    def wait_for_primary_bundles(self):
        Progress.report("WAITING FOR PRIMARY BUNDLE(s) TO BE CREATED...")
        self.expected_bundle_count = self.dataset.config["expected_bundle_count"]
        WaitFor(
            self._count_primary_bundles_and_report
        ).to_return_value(value=self.expected_bundle_count)

    def wait_for_analysis_workflows(self):
        if not self.analysis_agent:
            Progress.report("NO CREDENTIALS PROVIDED FOR ANALYSIS AGENT, SKIPPING WORKFLOW(s) CHECK...")
        else:
            Progress.report("WAITING FOR ANALYSIS WORKFLOW(s) TO FINISH...")
            WaitFor(
                self._count_analysis_workflows_and_report
            ).to_return_value(value=self.expected_bundle_count)
            
    def _count_analysis_workflows_and_report(self):
        if self._analysis_workflows_count() < self.expected_bundle_count:
            self._count_analysis_workflows()
        Progress.report("  successful analysis workflows: {}/{}".format(
            self._analysis_workflows_count(),
            self.expected_bundle_count
        ))
        return self._analysis_workflows_count()

    def _batch_count_analysis_workflows_by_project_shortname(self):
        """This should only be used for the scaling test"""
        # TODO: remove the following line once there are no more scalability concerns of the analysis agent
        with self.analysis_agent.ignore_logging_msg():
            try:
                workflows = self.analysis_agent.query_by_project_shortname(project_shortname=self.project_shortname, with_labels=False)
                self.analysis_workflow_set.update(workflows)
            except requests.exceptions.HTTPError:
                Progress.report("  something went wrong when querying workflows, skipping for this time...")

    def _count_analysis_workflows(self):
        for bundle_uuid in self.submission_envelope.bundles():
            # TODO: remove the following line once there are no more scalability concerns of the analysis agent
            with self.analysis_agent.ignore_logging_msg():
                try:
                    workflows = self.analysis_agent.query_by_bundle(bundle_uuid=bundle_uuid, with_labels=False)

                    # NOTE: this one-bundle-one-workflow mechanism might change in the future
                    if len(workflows) > 1:
                        raise Exception(f"Bundle {bundle_uuid} triggered more than one workflow: {workflows}")
                    elif len(workflows) == 1:
                        workflow = workflows[0]
                        if workflow.status in ('Failed', 'Aborted', 'Aborting'):
                            raise Exception(f"The status of workflow {workflow.uuid} is: {workflow.status}")
                        if workflow.status == 'Succeeded':
                            if workflow not in self.analysis_workflow_set:
                                Progress.report(f"    workflow succeeded for bundle {bundle_uuid}: \n     {workflow}")
                                self.analysis_workflow_set.add(workflow)
                        else:
                                Progress.report(f"    Found workflow for bundle {bundle_uuid}: \n     {workflow}")
                except requests.exceptions.HTTPError:
                    # Progress.report("ENCOUNTERED AN ERROR FETCHING WORKFLOW INFO, RETRY NEXT TIME...")
                    continue

    def wait_for_secondary_bundles(self):
        Progress.report("WAITING FOR RESULTS BUNDLE(s) TO BE CREATED...")
        self.expected_bundle_count = self.dataset.config["expected_bundle_count"]
        WaitFor(
            self._count_secondary_bundles_and_report
        ).to_return_value(value=self.expected_bundle_count)
    
    def _count_primary_bundles_and_report(self):
        if self._primary_bundle_count() < self.expected_bundle_count:
            self._count_primary_bundles()
        Progress.report("  bundles: primary: {}/{}".format(
            self._primary_bundle_count(),
            self.expected_bundle_count
        ))
        return self._primary_bundle_count()

    def _count_secondary_bundles_and_report(self):
        if self._results_bundles_count() < self.expected_bundle_count:
            self._count_results_bundles()
        Progress.report("  bundles: results: {}/{}".format(
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
    
    def _analysis_workflows_count(self):
        return len(self.analysis_workflow_set)

    def _ongoing_analysis_workflows_count(self):
        return len(
            list(filter(lambda wf: wf.status in ('Submitted', 'On Hold', 'Running'), self.analysis_workflow_set))
        )

    def _successful_analysis_workflows_count(self):
        return len(
            list(filter(lambda wf: wf.status == 'Succeeded', self.analysis_workflow_set))
        )

    def _failed_analysis_workflows_count(self):
        return len(
            list(filter(lambda wf: wf.status in ('Failed', 'Aborting', 'Aborted'), self.analysis_workflow_set))
        )

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
            files = self.azul_agent.get_entities_by_project('files', project_shortname)
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

    def _assert_project_removed_from_azul(self):
        results_empty = [len(self.azul_agent.get_entities_by_project(entity, self.project_shortname)) == 0
                         for entity in ['files', 'projects', 'specimens']]
        Progress.report("Project removed from index files: {}, projects: {}, specimens: {}".format(*results_empty))
        return all(results_empty)

    def cleanup_primary_and_result_bundles(self):
        for primary_bundle_uuid, secondary_bundle_fqid in self.primary_uuid_to_secondary_bundle_fqid_map.items():
            self.data_store.tombstone_bundle(primary_bundle_uuid)
            if secondary_bundle_fqid is not None:
                secondary_bundle_uuid = secondary_bundle_fqid.split('.')[0]
                self.data_store.tombstone_bundle(secondary_bundle_uuid)
        Progress.report("WAITING FOR BUNDLES TO BE REMOVED FROM AZUL ")
        WaitFor(
            self._assert_project_removed_from_azul
        ).to_return_value(True)

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

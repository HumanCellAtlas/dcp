#!/usr/bin/env python3

import glob
import json
import os
import re
import subprocess
import unittest

import iso8601
import requests
from urllib3.util import parse_url

from . import logger
from .utils import Progress
from .wait_for import WaitFor

DEPLOYMENTS = ('dev', 'staging', 'prod')


class LocalBundle:

    """
    Local test fixture bundles must be laid out as follows:
        bundle-folder/
            <some-spreadsheet>.xlsx
            data-files/
                <data_file_1>
                <data_file_2>
                ...
    """

    def __init__(self, bundle_path):
        self.bundle_path = bundle_path

    def metadata_spreadsheet_path(self):
        xlsx_files = glob.glob(f"{self.bundle_path}/*.xlsx")
        assert len(xlsx_files) == 1, f"There is more than 1 .xlsx file in {self.bundle_path}"
        return xlsx_files[0]

    def data_files_paths(self):
        return glob.glob(f"{self.bundle_path}/data-files/*")


class IngestBrokerAgent:

    INGEST_BROKER_URL_TEMPLATE = "http://ingest.{}.data.humancellatlas.org"

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_broker_url = self.INGEST_BROKER_URL_TEMPLATE.format(self.deployment)

    def upload(self, metadata_spreadsheet_path):
        url = self.ingest_broker_url + '/upload'
        files = {'file': open(metadata_spreadsheet_path, 'rb')}
        response = requests.post(url, files=files, allow_redirects=False)
        assert response.status_code == 302
        # Eventually this response will be a redirect that contains the submssion ID as a query param.
        # Meanwhile, let's do it the hard way:
        return self._get_most_recent_draft_submission_envelope_id()

    def _get_most_recent_draft_submission_envelope_id(self):
        submissions = IngestApiAgent(self.deployment).submissions()
        draft_submissions = [subm for subm in submissions if subm['submissionState'] == 'Draft']
        sorted_submissions = sorted(draft_submissions,
                                    key=lambda submission: iso8601.parse_date(submission['submissionDate']))
        newest_draft_submission = sorted_submissions[-1]
        submission_url = newest_draft_submission['_links']['self']['href']
        return parse_url(submission_url).path.split('/')[-1]


class IngestApiAgent:

    INGEST_API_URL_TEMPLATE = "http://api.ingest.{}.data.humancellatlas.org"

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_api_url = self.INGEST_API_URL_TEMPLATE.format(self.deployment)

    def submissions(self):
        url = self.ingest_api_url + '/submissionEnvelopes?size=1000'
        response = requests.get(url)
        return response.json()['_embedded']['submissionEnvelopes']

    def envelope(self, envelope_id=None):
        return IngestApiAgent.SubmissionEnvelope(envelope_id=envelope_id, ingest_api_url=self.ingest_api_url)

    class SubmissionEnvelope:

        def __init__(self, envelope_id=None, ingest_api_url=None):
            self.envelope_id = envelope_id
            self.ingest_api_url = ingest_api_url
            self.data = None
            if envelope_id:
                self._load()

        def staging_credentials(self):
            """ Return staging area credentials or None if this envelope doesn't have a staging area yet """
            staging_details = self.data.get('stagingDetails', None)
            if staging_details and 'stagingAreaLocation' in staging_details:
                return staging_details.get('stagingAreaLocation', {}).get('value', None)
            return None

        def reload(self):
            self._load()
            return self

        def status(self):
            return self.data['submissionState']

        def bundles(self):
            url = self.data['_links']['bundleManifests']['href']
            response = requests.get(url).json()
            return [bundleManifest['bundleUuid'] for bundleManifest in response['_embedded']['bundleManifests']]

        def _load(self):
            url = self.ingest_api_url + f'/submissionEnvelopes/{self.envelope_id}'
            self.data = requests.get(url).json()


class DataStoreAgent:

    DSS_API_URL_TEMPLATE = "http://dss.{deployment}.data.humancellatlas.org/v1"

    def __init__(self, deployment):
        self.deployment = deployment
        self.dss_url = self.DSS_API_URL_TEMPLATE.format(deployment=deployment)

    def search(self, query, replica='aws'):
        url = f"{self.dss_url}/search?replica={replica}"
        response = requests.post(url, json={"es_query": query})
        logger.debug(json.dumps(response.json(), indent=4))
        return response.json()['results']

    def download_bundle(self, bundle_uuid, target_folder):
        Progress.report(f"Downloading bundle {bundle_uuid}:\n")
        manifest = self.bundle_manifest(bundle_uuid)
        bundle_folder = os.path.join(target_folder, bundle_uuid)
        try:
            os.makedirs(bundle_folder)
        except FileExistsError:
            pass

        for f in manifest['bundle']['files']:
            self.download_file(f['uuid'], save_as=os.path.join(bundle_folder, f['name']))
        return bundle_folder

    def bundle_manifest(self, bundle_uuid, replica='aws'):
        url = f"{self.dss_url}/bundles/{bundle_uuid}?replica={replica}"
        response = requests.get(url)
        assert response.ok
        assert response.headers['Content-type'] == 'application/json'
        return json.loads(response.content)

    def download_file(self, file_uuid, save_as, replica='aws'):
        url = f"{self.dss_url}/files/{file_uuid}?replica={replica}"
        Progress.report(f"Downloading file {file_uuid} to {save_as}\n")
        response = requests.get(url, stream=True)
        assert response.ok
        with open(save_as, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)


class BundleRunner:

    def __init__(self, deployment):
        self.ingest_broker = IngestBrokerAgent(deployment=deployment)
        self.ingest_api = IngestApiAgent(deployment=deployment)
        self.data_store = DataStoreAgent(deployment=deployment)
        self.submission_id = None
        self.submission_envelope = None
        self.upload_credentials = None
        self.primary_bundle_uuid = None
        self.secondary_bundle_uuid = None

    def run(self, bundle):
        self.upload_spreadsheet_and_create_submission(bundle)
        self.get_staging_area_credentials()
        self.stage_data_files(bundle)
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

    def get_staging_area_credentials(self):
        Progress.report("WAITING FOR STAGING AREA...")
        self.upload_credentials = WaitFor(
            self._get_staging_area_credentials
        ).to_return_a_value_other_than(other_than_value=None, timeout_seconds=60)
        Progress.report(" credentials received.\n")

    def _get_staging_area_credentials(self):
        return self.submission_envelope.reload().staging_credentials()

    def stage_data_files(self, bundle):
        Progress.report("STAGING FILES...\n")
        self._run_command(['hca', 'upload', 'select', self.upload_credentials])
        for file_path in bundle.data_files_paths():
            self._run_command(['hca', 'upload', 'file', file_path])

    def wait_for_envelope_to_be_validated(self):
        Progress.report("WAIT FOR VALIDATION...")
        WaitFor(self._envelope_is_valid).to_return_value(value=True, timeout_seconds=5 * 60)
        Progress.report(" envelope is valid.\n")

    def _envelope_is_valid(self):
        return self.submission_envelope.reload().status() in ['Valid', 'Submitted']

    def complete_submission(self):
        Progress.report("COMPLETING SUBMISSION...")
        submit_url = self.submission_envelope.data['_links']['submit']['href']
        response = requests.put(submit_url)
        assert response.status_code == 202
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
                        "files.analysis_json.input_bundles": self.primary_bundle_uuid
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

    SMARTSEQ2_BUNDLE_PATH = 'tests/fixtures/bundles/Smart-seq2'
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

    def setUp(self):
        self.deployment = os.environ.get('TRAVIS_BRANCH', None)
        if self.deployment not in DEPLOYMENTS:
            raise RuntimeError(f"TRAVIS_BRANCH environment variable must be one of {DEPLOYMENTS}")
        self.data_store = DataStoreAgent(deployment=self.deployment)

    def test_smartseq2(self):
        bundle_fixture = LocalBundle(self.SMARTSEQ2_BUNDLE_PATH)
        runner = BundleRunner(deployment=self.deployment)
        runner.run(bundle_fixture)

        Progress.report("CHECKING RESULTS...\n")
        primary_bundle_manifest = self.data_store.bundle_manifest(runner.primary_bundle_uuid)
        primary_files_names = (file['name'] for file in primary_bundle_manifest['bundle']['files'])
        primary_files_regexes = (re.compile(f"^{re.escape(filename)}$") for filename in primary_files_names)

        expected_files_regexes = list(primary_files_regexes)
        expected_files_regexes += self.SS2_ANALYSIS_OUTPUT_FILES_REGEXES
        expected_files_regexes.append(re.compile('^analysis\.json$'))

        results_bundle_manifest = self.data_store.bundle_manifest(runner.secondary_bundle_uuid)

        self.check_manifest_contains_exactly_these_files(results_bundle_manifest, expected_files_regexes)

    def check_manifest_contains_exactly_these_files(self, bundle_manifest, filename_regexes):
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


if __name__ == '__main__':
    unittest.main()

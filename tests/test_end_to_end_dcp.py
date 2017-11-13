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
from .utils import progress
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
        progress(f"Downloading bundle {bundle_uuid}:\n")
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
        progress(f"Downloading file {file_uuid} to {save_as}\n")
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

    def run(self, bundle):
        envelope = self._upload_spreadsheet_and_create_submission(bundle)
        credentials = self._get_staging_area_credentials(envelope)
        self._stage_data_files(bundle, credentials)
        self._wait_for_envelope_to_be_validated(envelope)
        self._complete_submission(envelope)
        primary_bundle_uuid = self._wait_for_bundle_to_be_created(envelope)
        secondary_bundle_uuid = self._wait_for_results_bundle_to_be_created(primary_bundle_uuid)
        return secondary_bundle_uuid

    def _upload_spreadsheet_and_create_submission(self, bundle):
        progress("CREATING SUBMISSION...")
        envelope_id = self.ingest_broker.upload(bundle.metadata_spreadsheet_path())
        progress(f" submission ID is {envelope_id}\n")
        return self.ingest_api.envelope(envelope_id)

    def _get_staging_area_credentials(self, envelope):
        progress("WAITING FOR STAGING AREA...")
        credentials = WaitFor(
            self._staging_area_credentials, envelope
        ).to_return_a_value_other_than(other_than_value=None, timeout_seconds=60)
        progress(" credentials received.\n")
        return credentials

    def _staging_area_credentials(self, envelope):
        return envelope.reload().staging_credentials()

    def _stage_data_files(self, bundle, credentials):
        progress("STAGING FILES...\n")
        self._run_command(['hca', 'upload', 'select', credentials])
        for file_path in bundle.data_files_paths():
            self._run_command(['hca', 'upload', 'file', file_path])

    def _wait_for_envelope_to_be_validated(self, envelope):
        progress("WAIT FOR VALIDATION...")
        WaitFor(self._envelope_is_valid, envelope).to_return_value(value=True, timeout_seconds=5 * 60)
        progress(" envelope is valid.\n")

    def _envelope_is_valid(self, envelope):
        return envelope.reload().status() in ['Valid', 'Submitted']

    def _complete_submission(self, envelope):
        progress("COMPLETING SUBMISSION...")
        submit_url = envelope.data['_links']['submit']['href']
        response = requests.put(submit_url)
        assert response.status_code == 202
        progress(" done.\n")

    def _wait_for_bundle_to_be_created(self, envelope):
        progress("WAITING FOR PRIMARY BUNDLE UUID...")
        bundles = WaitFor(envelope.bundles).to_return_a_value_other_than(other_than_value=[], timeout_seconds=5*60)
        assert len(bundles) == 1
        primary_bundle_uuid = bundles[0]
        progress(f" {primary_bundle_uuid}\n")
        return primary_bundle_uuid

    def _wait_for_results_bundle_to_be_created(self, primary_bundle_uuid):
        progress("WAIT FOR RESULTS BUNDLE...")
        secondary_bundle_uuid = WaitFor(
            self._results_bundle, primary_bundle_uuid
        ).to_return_a_value_other_than(other_than_value=None, timeout_seconds=90*60)
        progress(f" {secondary_bundle_uuid}\n")
        return secondary_bundle_uuid

    def _results_bundle(self, primary_bundle_uuid):
        results = self.data_store.search(
            {
                "query": {
                    "match": {
                        "files.analysis_json.input_bundles": primary_bundle_uuid
                    }
                }
            }
        )
        if len(results) == 1:
            return results[0]['bundle_id']
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
    EXPECTED_FILES_IN_SS2_RESULT_BUNDLE_REGEXES = [
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

    def test_smartseq2(self):
        bundle_fixture = LocalBundle(self.SMARTSEQ2_BUNDLE_PATH)
        results_bundle_uuid = BundleRunner(deployment=self.deployment).run(bundle_fixture)
        bundle_manifest = DataStoreAgent(deployment='staging').bundle_manifest(results_bundle_uuid)
        self.check_ss2_results_bundle_manifest(bundle_manifest)

    def check_ss2_results_bundle_manifest(self, manifest):
        files = manifest['bundle']['files']
        self.assertEqual(len(files), len(self.EXPECTED_FILES_IN_SS2_RESULT_BUNDLE_REGEXES))
        for filename_regex in self.EXPECTED_FILES_IN_SS2_RESULT_BUNDLE_REGEXES:
            try:
                file_data = next((entry for entry in files if filename_regex.match(entry["name"])))
            except StopIteration:
                self.fail(f"couldn't find {filename_regex.pattern} in {list((f['name'] for f in files))}")
            self.assertGreater(file_data['size'], 0)


if __name__ == '__main__':
    unittest.main()

import iso8601
import requests
from urllib3.util import parse_url


class IngestUIAgent:

    INGEST_UI_URL_TEMPLATE = "http://ingest.{}.data.humancellatlas.org"

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_broker_url = self.INGEST_UI_URL_TEMPLATE.format(self.deployment)

    def upload(self, metadata_spreadsheet_path):
        url = self.ingest_broker_url + '/upload'
        files = {'file': open(metadata_spreadsheet_path, 'rb')}
        response = requests.post(url, files=files, allow_redirects=False)
        if response.status_code != requests.codes.found:
            raise RuntimeError(f"POST {url} response was {response.status_code}: {response.content}")
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

        def upload_credentials(self):
            """ Return upload area credentials or None if this envelope doesn't have an upload area yet """
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

import json
import requests
import os

from ingest.api.ingestapi import IngestApi
from ingest.utils.s2s_token_client import S2STokenClient
from ingest.utils.token_manager import TokenManager

_pluralized_type = {
    'biomaterial': 'biomaterials',
    'process': 'processes',
    'file': 'files',
    'project': 'projects',
    'protocol': 'protocols'
}

class IngestUIAgent:

    INGEST_UI_URL_TEMPLATE = "https://ingest.{}.data.humancellatlas.org"
    INGEST_UI_PROD_URL = "https://ingest.data.humancellatlas.org"

    def __init__(self, deployment):
        self.deployment = deployment
        if self.deployment == "prod":
            self.ingest_broker_url = self.INGEST_UI_PROD_URL
        else:
            self.ingest_broker_url = self.INGEST_UI_URL_TEMPLATE.format(self.deployment)
        self.ingest_auth_agent = IngestAuthAgent()

    def upload(self, metadata_spreadsheet_path):
        url = self.ingest_broker_url + '/api_upload'
        files = {'file': open(metadata_spreadsheet_path, 'rb')}
        headers = self.ingest_auth_agent.make_auth_header()
        response = requests.post(url, files=files, allow_redirects=False, headers=headers)
        if response.status_code != requests.codes.found and response.status_code != requests.codes.created:
            raise RuntimeError(f"POST {url} response was {response.status_code}: {response.content}")
        return json.loads(response.content)['details']['submission_id']


class IngestApiAgent:

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_api_url = self._ingest_api_url()
        self.ingest_auth_agent = IngestAuthAgent()
        self._set_up_ingest_client()

    def _set_up_ingest_client(self):
        self.ingest_api = IngestApi(url=self.ingest_api_url)
        auth_header = self.ingest_auth_agent.make_auth_header()
        self.ingest_api.set_token(auth_header['Authorization'])

    def project(self, project_id):
        return IngestApiAgent.Project(project_id=project_id, ingest_api_agent=self)

    def submission(self, submission_id):
        return IngestApiAgent.SubmissionEnvelope(envelope_id=submission_id, ingest_api_agent=self)

    def new_submission(self, is_update=False):
        submission_data = self.ingest_api.create_submission(update_submission=is_update)
        return IngestApiAgent.SubmissionEnvelope(ingest_api_agent=self, data=submission_data)

    def iter_submissions(self):
        for page in self.iter_pages('/submissionEnvelopes', page_size=500):
            for submission_data in page['submissionEnvelopes']:
                yield IngestApiAgent.SubmissionEnvelope(data=submission_data, ingest_api_agent=self)

    """
    Get a collection resource.
    Iterates through all pages gathering results and returns a list.
    """
    def get_all(self, path_or_url, result_element_we_are_interested_in):
        results = []
        for page in self.iter_pages(path_or_url):
            results += page[result_element_we_are_interested_in]
        return results

    """
    Iterate through a collection using HATEOAS pagination, yielding pages.
    """
    def iter_pages(self, path_or_url, page_size=100):
        path_or_url += f"?size={page_size}"

        while True:
            data = self.get(path_or_url)
            if '_embedded' not in data:
                break

            yield data['_embedded']

            if 'next' in data['_links']:
                path_or_url = data['_links']['next']['href']
            else:
                break

    """
    Get a singleton resource.
    """
    def get(self, path_or_url):
        if path_or_url.startswith('http'):
            url = path_or_url
        else:
            url = f"{self.ingest_api_url}{path_or_url}"

        response = requests.get(url, headers=self.ingest_auth_agent.make_auth_header())

        if response.ok:
            return response.json()
        else:
            raise RuntimeError(f"GET {url} got {response}")

    def post(self, url, content, params={}):
        auth_header = self.ingest_auth_agent.make_auth_header()
        response = requests.post(url, json=content, headers=auth_header, params=params)
        response.raise_for_status()
        return response.json()

    def _ingest_api_url(self):
        if self.deployment == 'prod':
            return "https://api.ingest.data.humancellatlas.org"
        else:
            return f"https://api.ingest.{self.deployment}.data.humancellatlas.org"

    class Project:

        def __init__(self, project_id, ingest_api_agent):
            self.project_id = project_id
            self.api = ingest_api_agent
            self.data = None
            self._load()

        @property
        def uuid(self):
            return self.data['uuid']

        def submission_envelopes(self):
            data = self.api.get(self.data['_links']['submissionEnvelopes']['href'])
            return [
                IngestApiAgent.SubmissionEnvelope(data=subm_data, ingest_api_agent=self.api) \
                for subm_data in data['_embedded']['submissionEnvelopes']
            ]

        def _load(self):
            self.data = self.api.get(f"/projects/{self.project_id}")

    class SubmissionEnvelope:

        # May be primed wih data, or of you supply an ID, we will go get the data
        def __init__(self, ingest_api_agent, envelope_id=None, data=None):
            if not envelope_id and not data:
                raise RuntimeError("either envelope_id or data must be provided")
            self.api = ingest_api_agent
            self.data = None
            if envelope_id:
                self.envelope_id = envelope_id
                self._load()
            else:
                self.data = data
                self.envelope_id = data['_links']['self']['href'].split('/')[-1]

        def __str__(self):
            return f"SubmissionEnvelope(id={self.envelope_id}, uuid={self.uuid}, " \
                f"status={self.status})"

        def _link_to(self, property):
            return self.data['_links'][property]['href']

        def files(self):
            return self.api.get_all(self.data['_links']['files']['href'], 'files')

        def metadata_documents(self, metadata_type: str = None):
            self._check_metadata_type(metadata_type)
            result_type = _pluralized_type[metadata_type]
            metadata_link = self._link_to(result_type)
            return self.api.get_all(metadata_link, result_type)

        def _add_metadata(self, metadata_type, metadata_content, update_target_uuid: str = None):
            self._check_metadata_type(metadata_type)
            endpoint_path = _pluralized_type[metadata_type]
            metadata_link = self._link_to(endpoint_path)
            params = {'updatingUuid': update_target_uuid} if update_target_uuid else {}
            self.api.post(metadata_link, metadata_content, params=params)

        def add_biomaterial(self, biomaterial_content, update_target_uuid: str = None):
            self._add_metadata('biomaterial', biomaterial_content,
                               update_target_uuid=update_target_uuid)

        @staticmethod
        def _check_metadata_type(metadata_type):
            if not metadata_type:
                raise RuntimeError('`metadata_type` must be specified')
            if not metadata_type in _pluralized_type:
                raise KeyError(f'Unknown metadata type [{metadata_type}].')

        def iter_files(self):
            url = self.data['_links']['files']['href']
            for page in self.api.iter_pages(url):
                for file in page['files']:
                    yield file

        def reload(self):
            self._load()
            return self

        @property
        def status(self):
            return self.data['submissionState']

        @property
        def uuid(self):
            return self.data['uuid']['uuid']

        def upload_credentials(self):
            """ Return upload area credentials or None if this envelope doesn't have an upload area yet """
            staging_details = self.data.get('stagingDetails', None)
            if staging_details and 'stagingAreaLocation' in staging_details:
                return staging_details.get('stagingAreaLocation', {}).get('value', None)
            return None

        def bundles(self):
            url = self.data['_links']['bundleManifests']['href']
            manifests = self.api.get_all(url, 'bundleManifests')
            return [manifest['bundleUuid'] for manifest in manifests]

        def _load(self):
            self.data = self.api.get(f"/submissionEnvelopes/{self.envelope_id}")


class IngestAuthAgent:
    def __init__(self):
        """This class controls the authentication actions with Ingest Service, including retrieving the token,
            store the token and make authenticated headers. Note:
        """
        self.s2s_token_client = S2STokenClient()
        gcp_credentials_file = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
        self.s2s_token_client.setup_from_file(gcp_credentials_file)
        self.token_manager = TokenManager(token_client=self.s2s_token_client)

    def get_auth_token(self):
        """Generate self-issued JWT token

        :return string auth_token: OAuth0 JWT token
        """
        auth_token = self.token_manager.get_token()
        return auth_token

    def make_auth_header(self):
        """Make the authorization headers to communicate with endpoints which implement Auth0 authentication API.

        :return dict headers: A header with necessary token information to talk to Auth0 authentication required endpoints.
        """
        headers = {
            "Authorization": f"Bearer {self.get_auth_token()}"
        }
        return headers


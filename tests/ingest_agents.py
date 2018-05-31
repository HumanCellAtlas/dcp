import json
import requests


class IngestUIAgent:

    INGEST_UI_URL_TEMPLATE = "http://ingest.{}.data.humancellatlas.org"

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_broker_url = self.INGEST_UI_URL_TEMPLATE.format(self.deployment)
        self.ingest_auth_agent = IngestAuthAgent()
        self.auth_headers = self.ingest_auth_agent.make_auth_header()

    def upload(self, metadata_spreadsheet_path):
        url = self.ingest_broker_url + '/api_upload'
        files = {'file': open(metadata_spreadsheet_path, 'rb')}
        response = requests.post(url, files=files, allow_redirects=False, headers=self.auth_headers)
        if response.status_code != requests.codes.found and response.status_code != requests.codes.created:
            raise RuntimeError(f"POST {url} response was {response.status_code}: {response.content}")
        return json.loads(response.content)['details']['submission_id']


class IngestApiAgent:

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_api_url = self._ingest_api_url()
        self.auth_headers = IngestAuthAgent().make_auth_header()

    def project(self, project_id):
        return IngestApiAgent.Project(project_id=project_id, ingest_api_agent=self)

    def submission(self, submission_id):
        return IngestApiAgent.SubmissionEnvelope(envelope_id=submission_id, ingest_api_agent=self)

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

        response = requests.get(url, headers=self.auth_headers)

        if response.ok:
            return response.json()
        else:
            raise RuntimeError(f"GET {url} got {response}")

    def _ingest_api_url(self):
        if self.deployment == 'prod':
            return "http://api.ingest.data.humancellatlas.org"
        else:
            return f"http://api.ingest.{self.deployment}.data.humancellatlas.org"

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
            return f"SubmissionEnvelope(id={self.envelope_id}, uuid={self.uuid}, status={self.status})"

        def files(self):
            return self.api.get_all(self.data['_links']['files']['href'], 'files')

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
    def __init__(self,
                 url="https://danielvaughan.eu.auth0.com/oauth/token",
                 client_id="Zdsog4nDAnhQ99yiKwMQWAPc2qUDlR99",
                 client_secret="t-OAE-GQk_nZZtWn-QQezJxDsLXmU7VSzlAh9cKW5vb87i90qlXGTvVNAjfT9weF",
                 audience="http://localhost:8080",
                 grant_type="client_credentials"):
        """This class controls the authentication actions with Ingest Service, including retrieving the token,
            store the token and make authenticated headers. Note: The parameters and credentials here are
            meant to be hard coded, the authentication is purely for identifying a user it doesn't give any permissions.

        :param str url: The url to the Auth0 domain oauth endpoint.
        :param str client_id: The value of the Client ID field of the Non Interactive Client of Auth0.
        :param str client_secret: The value of the Client Secret field of the Non Interactive Client of Auth0.
        :param str audience: The value of the Identifier field of the Auth0 Management API.
        :param str grant_type: Denotes which OAuth 2.0 flow you want to run. e.g. client_credentials
        """
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.audience = audience
        self.grant_type = grant_type
        self.auth_token = self._get_auth_token()

    def _get_auth_token(self):
        """Request and get the access token for a trusted client from Auth0.

        :return dict auth_token: JSON response of the signed JWT (JSON Web Token), with when it expires (24h by default),
            the scopes granted, and the token type.
        """
        url = self.url
        headers = {
            "content-type": "application/json"
        }
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "audience": self.audience,
            "grant_type": self.grant_type
        }
        response = requests.post(url=url, headers=headers, json=payload)
        response.raise_for_status()
        auth_token = response.json()
        return auth_token

    def make_auth_header(self):
        """Make the authorization headers to communicate with endpoints which implement Auth0 authentication API.

        :return dict headers: A header with necessary token information to talk to Auth0 authentication required endpoints.
        """
        token_type = self.auth_token['token_type']
        access_token = self.auth_token['access_token']

        headers = {
            "Authorization": f"{token_type} {access_token}"
        }
        return headers

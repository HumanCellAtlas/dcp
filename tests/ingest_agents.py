import iso8601
import requests
from urllib3.util import parse_url


class IngestUIAgent:

    INGEST_UI_URL_TEMPLATE = "http://ingest.{}.data.humancellatlas.org"

    def __init__(self, deployment):
        self.deployment = deployment
        self.ingest_broker_url = self.INGEST_UI_URL_TEMPLATE.format(self.deployment)
        self.ingest_auth_agent = IngestAuthAgent()
        self.auth_headers = self.ingest_auth_agent.make_auth_header()


    def upload(self, metadata_spreadsheet_path):
        url = self.ingest_broker_url + '/upload'
        files = {'file': open(metadata_spreadsheet_path, 'rb')}
        response = requests.post(url, files=files, allow_redirects=False, headers = self.auth_headers)
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
        self.ingest_auth_agent = IngestAuthAgent()
        self.auth_headers = self.ingest_auth_agent.make_auth_header()

    def submissions(self):
        url = self.ingest_api_url + '/submissionEnvelopes?size=1000'
        response = requests.get(url, headers = self.auth_headers)
        return response.json()['_embedded']['submissionEnvelopes']

    def envelope(self, envelope_id=None):
        return IngestApiAgent.SubmissionEnvelope(envelope_id=envelope_id, ingest_api_url=self.ingest_api_url,
                                                 auth_headers = self.auth_headers)

    class SubmissionEnvelope:

        def __init__(self, envelope_id=None, ingest_api_url=None, auth_headers=None):
            self.envelope_id = envelope_id
            self.ingest_api_url = ingest_api_url
            self.data = None
            self.auth_headers = auth_headers
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
            response = requests.get(url, headers = self.auth_headers).json()
            return [bundleManifest['bundleUuid'] for bundleManifest in response['_embedded']['bundleManifests']]

        def _load(self):
            url = self.ingest_api_url + f'/submissionEnvelopes/{self.envelope_id}'
            self.data = requests.get(url, headers = self.auth_headers).json()


class IngestAuthAgent:
    def __init__(self,
                 url="https://danielvaughan.eu.auth0.com/oauth/token",
                 client_id="Zdsog4nDAnhQ99yiKwMQWAPc2qUDlR99",
                 client_secret="t-OAE-GQk_nZZtWn-QQezJxDsLXmU7VSzlAh9cKW5vb87i90qlXGTvVNAjfT9weF",
                 audience="http://localhost:8080",
                 grant_type="client_credentials"):
        """This class controls the authentication actions with Ingest Service, including retrieving the token,
            store the token and make authenticated headers.

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
        """Request and get the access token for a trusted client from Auth0. Note: The parameters and credentials here are
            meant to be hard coded, the authentication is purely for identifying a user it doesn't give and permissions.

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
            "Content-type": "application/json",
            "Authorization": f"{token_type} {access_token}"
        }
        return headers
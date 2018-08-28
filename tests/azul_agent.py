import json
import requests
import urllib.parse


class AzulAgent:
    AZUL_URL_TEMPLATE = 'https://service.{deployment}.explore.data.humancellatlas.org'

    def __init__(self, deployment):
        from urllib3 import Retry
        self.azul_url = self.AZUL_URL_TEMPLATE.format(deployment=deployment)
        self.https_session = requests.Session()
        azul_retries = Retry(status_forcelist=(500, 502, 503, 504))
        azul_adapter = requests.adapters.HTTPAdapter(max_retries=azul_retries)
        self.https_session.mount('https://', azul_adapter)

    def get_specimen_by_project(self, project_shortname):
        filters = {"file": {"project": {"is": [project_shortname]}}}
        path = '/repository/specimens?filters=' + urllib.parse.quote(json.dumps(filters))
        response = self.https_session.request("GET", self.azul_url + path)
        response.raise_for_status()
        return response.json()

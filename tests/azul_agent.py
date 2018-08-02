import json
import requests
import urllib.parse


class AzulAgent:
    AZUL_URL_TEMPLATE = 'https://service.{deployment}.explore.data.humancellatlas.org'

    def __init__(self, deployment):
        self.azul_url = self.AZUL_URL_TEMPLATE.format(deployment=deployment)

    def get_specimen_by_project(self, project_shortname):
        filters = {"file": {"project": {"is": [project_shortname]}}}
        path = '/repository/specimens?filters=' + urllib.parse.quote(json.dumps(filters))
        response = requests.get(self.azul_url + path)
        response.raise_for_status()
        return response.json()

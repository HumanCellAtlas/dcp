import json
import requests


class AzulAgent:
    AZUL_URL_TEMPLATE = 'https://service.{deployment}.explore.data.humancellatlas.org'
    AZUL_PROD_URL = 'https://service.explore.data.humancellatlas.org'

    def __init__(self, deployment):
        from urllib3 import Retry
        if deployment == "prod":
            self.azul_url = self.AZUL_PROD_URL
        else:
            self.azul_url = self.AZUL_URL_TEMPLATE.format(deployment=deployment)
        self.https_session = requests.Session()
        azul_retries = Retry(status_forcelist=(500, 502, 503, 504))
        azul_adapter = requests.adapters.HTTPAdapter(max_retries=azul_retries)
        self.https_session.mount('https://', azul_adapter)

    def get_entities_by_project(self, entity_type, project_shortname):
        """
        Returns all files in a given project.

        >>> agent = AzulAgent(deployment='prod')
        >>> files = agent.get_entities_by_project('files', '')
        >>> len(files) == 0
        True
        """
        filters = {'project': {'is': [project_shortname]}}
        files = []
        size = 100
        params = dict(filters=json.dumps(filters), size=str(size))
        while True:
            url = self.azul_url + f'/repository/{entity_type}'
            response = self.https_session.request('GET', url, params=params)
            response.raise_for_status()
            body = response.json()
            hits = body['hits']
            files.extend(hits)
            pagination = body['pagination']
            search_after = pagination['search_after']
            if search_after is None:
                break
            params['search_after'] = search_after
            params['search_after_uid'] = pagination['search_after_uid']
        return files

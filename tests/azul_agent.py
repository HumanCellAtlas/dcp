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

    def get_files_py_project(self, project_shortname):
        """
        Returns all files in a given project.

        >>> agent = AzulAgent(deployment='staging')
        >>> files = agent.get_files_py_project('integration/10x/2018-11-07T16:01:15Z')
        >>> len(files) > 0
        True
        """
        filters = {'file': {'project': {'is': [project_shortname]}}}
        files = []
        size = 100
        # Yes, the value of the filters parameter is a Python literal, not JSON.
        # https://github.com/DataBiosphere/azul/issues/537
        params = dict(filters=str(filters), size=str(size))
        while True:
            url = self.azul_url + '/repository/files?' + urllib.parse.urlencode(params, safe="{}/'")
            response = self.https_session.request('GET', url)
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

import json
import os

import requests

from . import logger
from .utils import Progress


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

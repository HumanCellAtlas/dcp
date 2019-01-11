import json
import os

from hca.dss import DSSClient
from hca.util.exceptions import SwaggerAPIException

from . import logger
from .utils import Progress


class DataStoreAgent:

    DSS_SWAGGER_URL_TEMPLATE = "https://dss.{deployment}.data.humancellatlas.org/v1/swagger.json"

    def __init__(self, deployment):
        self.deployment = deployment
        swagger_url = self.DSS_SWAGGER_URL_TEMPLATE.format(deployment=deployment)
        self.client = DSSClient(swagger_url=swagger_url)

    def search(self, query, replica='aws'):
        try:
            response = self.client.post_search(replica=replica, es_query=query)
            return response['results']
        except SwaggerAPIException:
            return []

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
        return self.client.get_bundle(replica=replica, uuid=bundle_uuid)

    def download_file(self, file_uuid, save_as, replica='aws'):
        Progress.report(f"Downloading file {file_uuid} to {save_as}\n")
        with self.client.get_file.stream(replica=replica, uuid=file_uuid) as fh:
            with open(save_as, "wb") as f:
                while True:
                    chunk = fh.raw.read(1024)
                    if chunk:
                        f.write(chunk)
                    else:
                        break

    def tombstone_bundle(self, bundle_uuid, replica='aws'):
        self.client.delete_bundle(replica=replica, uuid=bundle_uuid, reason="DCP-wide integration test")

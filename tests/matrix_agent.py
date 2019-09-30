import requests
import json

from .utils import Progress


class MatrixAgent:
    MATRIX_URL_TEMPLATE = 'https://matrix.{deployment}.data.humancellatlas.org/v1'
    MATRIX_PROD_URL = 'https://matrix.data.humancellatlas.org/v1'

    def __init__(self, deployment):
        self.deployment = deployment
        if self.deployment == "prod":
            self.service_url = self.MATRIX_PROD_URL
        else:
            self.service_url = self.MATRIX_URL_TEMPLATE.format(deployment=deployment)
        self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

    def post_matrix_request(self, bundle_fqids, format="loom"):
        data = {
            'filter': self._generate_request_filter(bundle_fqids),
            'format': format
        }
        response = requests.post(f"{self.service_url}/matrix",
                                 data=json.dumps(data),
                                 headers=self.headers)
        data = response.json()
        request_id = data["request_id"]
        Progress.report(f"CREATED MATRIX REQUEST with request id {request_id}...")
        return request_id

    def get_matrix_request(self, request_id):
        url = f"{self.service_url}/matrix/{request_id}"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        status = data["status"]
        return status

    def is_matrix_project_indexed(self, project_short_name):
        res = requests.get(f"{self.service_url}/filters/project.project_core.project_short_name", headers=self.headers)
        content = res.json()

        return project_short_name in content['cell_counts']

    @staticmethod
    def _generate_request_filter(bundle_fqids):
        assert bundle_fqids

        bundle_uuids = [bundle_fqid.split(".", 1)[0] for bundle_fqid in bundle_fqids]

        if len(bundle_uuids) == 1:
            return {
                'op': "=",
                'field': "bundle_uuid",
                'value': bundle_uuids[0]
            }
        else:
            return {
                'op': "or",
                'value': [
                    {
                        'op': "=",
                        'field': "bundle_uuid",
                        'value': bundle_uuid
                    } for bundle_uuid in bundle_uuids
                ]
            }
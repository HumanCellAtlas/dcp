import requests
from urllib3 import Retry
import json

from .utils import Progress


class MatrixAgent:
    MATRIX_URL_TEMPLATE = 'https://matrix.{deployment}.data.humancellatlas.org/v0'

    def __init__(self, deployment):
        self.deployment = deployment
        self.service_url = self.MATRIX_URL_TEMPLATE.format(deployment=deployment)
        self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

    def post_matrix_request(self, bundle_fqids, format="zarr"):
        data = {}
        data['bundle_fqids'] = bundle_fqids
        data['format'] = format
        response = requests.post(f"{self.service_url}/matrix",
                                 data=json.dumps(data),
                                 headers=self.headers)
        data = response.json()
        request_id = data["request_id"]
        Progress.report(f"CREATED MATRIX REQUEST with request id {request_id}...")
        return data["request_id"]

    def get_matrix_request(self, request_id):
        url = f"{self.service_url}/matrix/{request_id}"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        status = data["status"]
        return status
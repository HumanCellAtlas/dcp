import os
import typing
from enum import Enum

import boto3


class CloudwatchHandler:
    def __init__(self):
        self.namespace = f"dcp-dcp-test-{os.environ['DEPLOYMENT_STAGE']}"
        self._client = boto3.client("cloudwatch", region_name=os.environ['AWS_DEFAULT_REGION'])

    def put_metric_data(self,
                        metric_name,
                        metric_value):
        """
        Puts a cloudwatch metric data point
        :param metric_name: The name of the metric to put
        :param metric_value: value of metric to put
        """
        metric_data = {
            'MetricName': metric_name,
            'Value': metric_value
        }

        self._client.put_metric_data(MetricData=[metric_data], Namespace=self.namespace)

from cromwell_tools import api as cwm_api
from cromwell_tools import cromwell_auth as cwm_auth
from .analysis_entities import Workflow
from contextlib import contextmanager
import logging


class AnalysisAgent:
    def __init__(self, deployment, service_account_key):
        """Agent model for talking to the HCA DCP Secondary-analysis service.

        This model is designed to talk to the HCA DCP Secondary-analysis service, especially the underlying Cromwell
            Workflow Execution Engine's API without exposing too many technical details to the users.

        Args:
            deployment (str): String representing the deployment environment to be queried on. It could be:
                "dev", "integration", "staging" or "prod".
            service_account_key (str): Optional, path to the service account JSON key file, which is required by
                authenticate with the Secondary-analysis service (Crowmell API). If not provided, the agent will assume
                no authentication required for talking to secondary analysis, which is very likely to break or skip
                a lot of commands that are using this agent.
                TODO: Add OAuth support to this agent so that users could authenticate through Google/Auth0.
        """
        self.deployment = deployment
        self.cromwell_url = 'https://cromwell.caas-prod.broadinstitute.org'
        self.cromwell_collection = 'lira-test' if self.deployment == 'integration' else f'lira-{self.deployment}'
        self.auth = self._get_auth(service_account_key)

    def _get_auth(self, service_account_key):
        """Helper function to generate the auth object to talk to Secondary-analysis service."""
        return cwm_auth.CromwellAuth.harmonize_credentials(service_account_key=service_account_key,
                                                           url=self.cromwell_url)

    @staticmethod
    @contextmanager
    def ignore_logging_msg(highest_level=logging.CRITICAL):
        """A context manager that will prevent any logging messages triggered during the body from being processed.

        Referred to https://gist.github.com/simon-weber/7853144
        two kind-of hacks here:
            * can't get the highest logging level in effect => delegate to the user
            * can't get the current module-level override => use an undocumented (but non-private!) interface

        highest_level (int): The maximum logging level in use. This would only need to be changed if
            a custom level greater than CRITICAL is defined.
        """
        previous_level = logging.root.manager.disable

        logging.disable(highest_level)

        try:
            yield
        finally:
            logging.disable(previous_level)

    def query_by_workflow_uuid(self, uuid):
        """Query an analysis workflow by its workflow-UUID.

        It is a one to one mapping between UUID and workflow in Secondary-analysis service (Cromwell), so the
        result should always be a single workflow. The Workflow object returned by this function will look like an
        object be loaded from the following dictionary:

            {
                "end": "2019-01-06T20:35:19.533Z",
                "id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                "labels": {
                    "bundle-uuid": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "bundle-version": "2018-11-02T114842.872218Z",
                    "caas-collection-name": "xxxx-prod",
                    "cromwell-workflow-id": "cromwell-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "project_shortname": "project name",
                    "project_uuid": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "workflow-name": "AdapterSmartSeq2SingleCell",
                    "workflow-version": "smartseq2_v2.1.0"
                },
                "name": "AdapterSmartSeq2SingleCell",
                "start": "2019-01-06T20:18:18.102Z",
                "status": "Succeeded",
                "submission": "2019-01-06T20:16:30.804Z"
            }

        Args:
            uuid (str): Secondary-analysis service (Cromwell) workflow UUID.

        Returns:
            Workflow: Workflow object.

        Raises:
            requests.exceptions.HTTPError: When the request to Secondary-analysis service (Cromwell) failed.
        """
        query_dict = {
            'id': uuid,
            'additionalQueryResultFields': ['labels']
        }
        
        query_dict['label']['caas-collection-name'] = self.cromwell_collection

        response = cwm_api.query(query_dict=query_dict, auth=self.auth)
        response.raise_for_status()
        result = response.json()
        all_workflows = result['results']
        total_count = result['totalResultsCount']
        assert len(all_workflows) == total_count == 1
        return Workflow(all_workflows[0])

    def query_by_bundle(self, bundle_uuid, bundle_version=None, with_labels=True):
        """Query the analysis workflows by their workflow-UUID.

        Note, due to the open issue: https://github.com/broadinstitute/cromwell/issues/3115, if the result of workflows
        are more than ~1000, this function will very likely raise an error.

        Args:
            bundle_uuid (str): HCA DCP bundle UUID.
            bundle_version (str): Optional, HCA DCP bundle version. By default, it's None.
            with_labels (bool): Optional, whether to return workflow labels in the results. By default, it's False.

        Returns:
            List[Workflow]: A list of Workflow objects. E.g. [Workflow_1, ..., Workflow_100]

        Raises:
            requests.exceptions.HTTPError: When the request to Secondary-analysis service (Cromwell) failed.
        """
        query_dict = {
            'label': {
                'bundle-uuid': bundle_uuid
            }
        }

        if additional_query_result_fields:
            query_dict['additionalQueryResultFields'] = ['labels']

        if bundle_version:
            query_dict['label']['bundle-version'] = bundle_version
        
        query_dict['label']['caas-collection-name'] = self.cromwell_collection

        response = cwm_api.query(query_dict=query_dict, auth=self.auth)
        response.raise_for_status()
        result = response.json()
        all_workflows = [Workflow(wf) for wf in result['results']]
        return all_workflows

    def query_by_project_uuid(self, project_uuid, with_labels=True):
        """Query the analysis workflows by the HCA DCP Ingest submission project-UUID, which is essentially one of the
            workflow labels.

        Note, due to the open issue: https://github.com/broadinstitute/cromwell/issues/3115, if the result of workflows
        are more than ~1000, this function will very likely raise an error. The `with_labels` is a flag controlling the
        behavior of whether to query the workflows asking for the labels in the response, by default it's set to True,
        so please set it to False if you don't want to risk getting error responses.

        Args:
            project_uuid (str): HCA DCP Ingest submission project-UUID.
            with_labels (bool): Optional, whether to return workflow labels in the results. By default, it's False.

        Returns:
            List[Workflow]: A list of Workflow objects. E.g. [Workflow_1, ..., Workflow_100]

        Raises:
            requests.exceptions.HTTPError: When the request to Secondary-analysis service (Cromwell) failed.
        """
        query_dict = {
            "label": {
                "project_uuid": project_uuid
            }
        }
        if with_labels:
            query_dict['additionalQueryResultFields'] = ['labels']
        
        query_dict['label']['caas-collection-name'] = self.cromwell_collection

        response = cwm_api.query(query_dict=query_dict, auth=self.auth)
        response.raise_for_status()
        result = response.json()
        all_workflows = [Workflow(wf) for wf in result['results']]
        return all_workflows

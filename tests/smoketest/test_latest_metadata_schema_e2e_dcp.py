import os
import unittest

from ingest.template.new_schema_template import NewSchemaTemplate
from ingest.template.vanilla_spreadsheet_builder import VanillaSpreadsheetBuilder

from ..dataset_fixture import DatasetFixture
from ..dataset_runner import DatasetRunner


class TestLatestMetadataSchemaE2EDcp(unittest.TestCase):

    def test_latest_metadata(self):
        fixture_name = "latest_metadata"
        self.generate_temporary_dataset(fixture_name)
        self._run(fixture_name=fixture_name)

    def generate_temporary_dataset(self, fixture_name):
        """ Generate bogus metadata based on the latest metadata schemas and store it as a temporary file fixture. """
        dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures/datasets', fixture_name))

        # Create a SchemaTemplate object that encapsulates information about the latest set of metadata schemas.
        ingest_api_url = "http://api.ingest." + os.environ['CI_COMMIT_REF_NAME'] + ".data.humancellatlas.org"
        property_migrations_url = "https://schema." + os.environ[
            'CI_COMMIT_REF_NAME'] + ".data.humancellatlas.org/property_migrations"
        metadata_schema_template = NewSchemaTemplate(ingest_api_url=ingest_api_url,
                                                     migrations_url=property_migrations_url)

        # Given the SchemaTemplate that represents all schemas, generate a spreadsheet
        spreadsheet_builder = VanillaSpreadsheetBuilder(output_file_name=dataset_path, hide_row=True)
        spreadsheet_builder.generate_spreadsheet(schema_template=metadata_schema_template)
        spreadsheet_builder.save_spreadsheet()

    def _run(self, fixture_name, export_bundles=True):
        print("")
        dataset = DatasetFixture(fixture_name, deployment=os.environ['CI_COMMIT_REF_NAME'])
        runner = DatasetRunner(deployment=os.environ['CI_COMMIT_REF_NAME'], export_bundles=export_bundles)
        runner.run(dataset_fixture=dataset)

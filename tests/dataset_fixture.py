import json
import os
import glob


class DatasetFixture:

    """
    Local test fixture datasets must be laid out as follows:
         dataset-folder/
            <some-spreadsheet>.xlsx
            data-files/
                <data_file_1>
                <data_file_2>
                ...

    Spreadsheet names must include a version string _v<x>_ e.g. "_v5_".
    """

    def __init__(self, dataset_name):
        self.config = {}
        self.dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures/datasets', dataset_name))
        readme_json_path = os.path.join(self.dataset_path, 'README.json')
        if os.path.isfile(readme_json_path):
            with open(readme_json_path) as json_data:
                self.config = json.load(json_data)

    def data_files_are_local(self):
        return not self.data_files_are_in_s3()

    def data_files_are_in_s3(self):
        return self.config.get('data_files_location', '').startswith('s3://')

    @property
    def metadata_spreadsheet_path(self, metadata_version="5"):
        xlsx_files = glob.glob(f"{self.dataset_path}/*_v{metadata_version}_*.xlsx")
        assert len(xlsx_files) == 1, f"There is more than 1 .xlsx file in {self.dataset_path}"
        return xlsx_files[0]

    def data_files_paths(self):
        return glob.glob(f"{self.dataset_path}/data-files/*")

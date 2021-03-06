import json
import os

import openpyxl
import requests
import validators


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

    def __init__(self, dataset_name, deployment):
        self.name = dataset_name
        if deployment == "prod":
            # Metadata uses master branch for prod schemas
            self.deployment = "master"
        else:
            self.deployment = deployment
        self.config = {}
        self.dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures/datasets', self.name))
        self._spreadsheet = None
        readme_json_path = os.path.join(self.dataset_path, 'README.json')
        with open(readme_json_path) as json_data:
            self.config = json.load(json_data)
            self.config["spreadsheet_location"] = self.config["spreadsheet_location"].replace("DEPLOYMENT",
                                                                                              self.deployment)
        if validators.url(self.config["spreadsheet_location"]):
            self._download_spreadsheet()

    def _download_spreadsheet(self):
        response = requests.get(self.config["spreadsheet_location"])
        with open(self.metadata_spreadsheet_path, 'wb') as f:
            f.write(response.content)

    def update_spreadsheet_project_shortname(self, new_shortname):
        project_tab = self.spreadsheet['Project']
        if project_tab['A4'].value != "project.project_core.project_short_name":
            raise RuntimeError("Project shortname is no longer in cell project!A2")
        project_tab['A6'] = new_shortname
        self.spreadsheet.save(filename=self.metadata_spreadsheet_path)

    @property
    def metadata_spreadsheet_path(self):
        filename = self.name + '.xlsx'
        return os.path.join(self.dataset_path, filename)

    @property
    def spreadsheet(self):
        if not self._spreadsheet:
            self._spreadsheet = openpyxl.load_workbook(self.metadata_spreadsheet_path)
        return self._spreadsheet

    def count_of_rows_in_spreadsheet_tab(self, tab_name, header_rows=5):
        ws = self.spreadsheet[tab_name]
        rows_with_content = 0
        row = header_rows + 1
        while ws.cell(row=row, column=1).value:
            rows_with_content += 1
            row += 1
        return rows_with_content

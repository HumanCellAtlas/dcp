import json
import os
import glob

import boto3
import openpyxl
import requests
from hca.util.pool import ThreadPool


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
            self.config["spreadsheet_location"] = self.config["spreadsheet_location"].replace("DEPLOYMENT", self.deployment)
        self._download_spreadsheet()
        if self.config["generate_scaled_spreadsheet"] == True:
            self._generate_scaled_spreadsheet_and_data_files()

    def _generate_scaled_spreadsheet_and_data_files(self):
        self._scale_spreadsheet_cell_suspensions()
        self._scale_sequence_files()

    def _scale_spreadsheet_cell_suspensions(self):
        cell_suspension_tab = self.spreadsheet['Cell suspension']
        row_to_copy = self._fetch_row_with_headers(cell_suspension_tab, 6)
        num_rows_to_copy = self.config["expected_bundle_count"]
        for row_idx in range(2, num_rows_to_copy + 1):
            new_row = row_to_copy.copy()
            new_row["cell_suspension.biomaterial_core.biomaterial_id"] = row_to_copy["cell_suspension.biomaterial_core.biomaterial_id"].replace("1", str(row_idx))
            new_row["cell_suspension.plate_based_sequencing.plate_id"] = row_to_copy["cell_suspension.plate_based_sequencing.plate_id"] + 1
            new_row["cell_suspension.plate_based_sequencing.well_id"] = f"A{row_idx}"
            cell_suspension_tab.append(list(new_row.values()))
        self.spreadsheet.save(filename=self.metadata_spreadsheet_path)

    def _scale_sequence_files(self):
        sequence_file_tab = self.spreadsheet['Sequence file']
        first_file_row_to_copy = self._fetch_row_with_headers(sequence_file_tab, 6)
        second_file_row_to_copy = self._fetch_row_with_headers(sequence_file_tab, 7)
        num_rows_to_copy = self.config["expected_bundle_count"]
        orig_filename_1 = first_file_row_to_copy['sequence_file.file_core.file_name']
        orig_filename_2 = second_file_row_to_copy['sequence_file.file_core.file_name']
        pool = ThreadPool()
        pool.add_task(self._copy_sequence_file, orig_filename_1, orig_filename_1)
        pool.add_task(self._copy_sequence_file, orig_filename_2, orig_filename_2)
        for row_idx in range(2, num_rows_to_copy + 1):
            new_first_file_row = first_file_row_to_copy.copy()
            new_second_file_row = second_file_row_to_copy.copy()
            new_filename_1 = f"{row_idx}_{orig_filename_1}"
            new_filename_2 = f"{row_idx}_{orig_filename_2}"
            new_first_file_row["sequence_file.file_core.file_name"] = new_filename_1
            new_second_file_row["sequence_file.file_core.file_name"] = new_filename_2
            new_first_file_row["cell_suspension.biomaterial_core.biomaterial_id"] = first_file_row_to_copy['cell_suspension.biomaterial_core.biomaterial_id'].replace("1", str(row_idx))
            new_second_file_row["cell_suspension.biomaterial_core.biomaterial_id"] = second_file_row_to_copy['cell_suspension.biomaterial_core.biomaterial_id'].replace("1", str(row_idx))
            new_first_file_row["process.process_core.process_id"] = row_idx
            new_second_file_row["process.process_core.process_id"] = row_idx
            sequence_file_tab.append(list(new_first_file_row.values()))
            sequence_file_tab.append(list(new_second_file_row.values()))
            pool.add_task(self._copy_sequence_file, orig_filename_1, new_filename_1)
            pool.add_task(self._copy_sequence_file, orig_filename_2, new_filename_2)
        pool.wait_for_completion()
        self.spreadsheet.save(filename=self.metadata_spreadsheet_path)

    def _copy_sequence_file(self, source_file_name, target_file_name):
        s3_client = boto3.client('s3')
        source_s3_prefix = self.config["orig_copy_files_location"]
        source_s3_path = f"{source_s3_prefix}{source_file_name}"
        s3_path_split = source_s3_path.replace("s3://", "").split("/", 1)
        source_bucket = s3_path_split[0]
        source_key = s3_path_split[1]

        target_s3_prefix = self.config["data_files_location"]
        target_s3_path = f"{target_s3_prefix}{target_file_name}"
        s3_path_split = target_s3_path.replace("s3://", "").split("/", 1)
        target_bucket = s3_path_split[0]
        target_key = s3_path_split[1]

        copy_source = {
            'Bucket': source_bucket,
            'Key': source_key
        }
        upload_args = {
            'CopySource': copy_source,
            'Bucket': target_bucket,
            'Key': target_key
        }
        print(f"copying {source_s3_path} to {target_s3_path}")
        s3_client.copy(**upload_args)

    def _fetch_row_with_headers(self, worksheet, row_idx):
        row = {}
        headers = self._fetch_row_values(worksheet, "A4:AG4")
        value_idxs = f"A{row_idx}:AG{row_idx}"
        values = self._fetch_row_values(worksheet, value_idxs)
        for idx, val in enumerate(headers):
            row[val] = values[idx]
        return row

    def _fetch_row_values(self, ws, n):
        values = []
        for row in ws.iter_rows(n):
            for cell in row:
                values.append(cell.value)
        return values

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
        extra_rows_to_check = 10
        while extra_rows_to_check > 0:
            if ws.cell(row=row, column=1).value:
                rows_with_content += 1
            else:
                extra_rows_to_check -= 1
            row += 1
        return rows_with_content

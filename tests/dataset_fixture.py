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
    """

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    @property
    def metadata_spreadsheet_path(self):
        xlsx_files = glob.glob(f"{self.dataset_path}/*_v5_*.xlsx")
        assert len(xlsx_files) == 1, f"There is more than 1 .xlsx file in {self.dataset_path}"
        return xlsx_files[0]

    def data_files_paths(self):
        return glob.glob(f"{self.dataset_path}/data-files/*")

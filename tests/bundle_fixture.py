import glob


class BundleFixture:

    """
    Local test fixture bundles must be laid out as follows:
        bundle-folder/
            <some-spreadsheet>.xlsx
            data-files/
                <data_file_1>
                <data_file_2>
                ...
    """

    def __init__(self, bundle_path):
        self.bundle_path = bundle_path

    @property
    def metadata_spreadsheet_path(self):
        xlsx_files = glob.glob(f"{self.bundle_path}/*_v5_*.xlsx")
        assert len(xlsx_files) == 1, f"There is more than 1 .xlsx file in {self.bundle_path}"
        return xlsx_files[0]

    def data_files_paths(self):
        return glob.glob(f"{self.bundle_path}/data-files/*")

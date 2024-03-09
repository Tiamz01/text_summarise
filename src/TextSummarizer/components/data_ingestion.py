import os
from pathlib import Path
import urllib.request  as request
import zipfile
from TextSummarizer.logging.logger import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity.entity import DataIngestionConfig

# component
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloading with the folowing info: \n{headers}")

        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")


    def extract_zipfile(self):
        """
        Extracts the zip file to the data directory.
    
        Args:
            unzip_path (Path): The directory where the zip file is to be extracted.
    
        Raises:
            FileNotFoundError: If the zip file does not exist.
            NotADirectoryError: If the unzip directory already exists and is not a directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
        
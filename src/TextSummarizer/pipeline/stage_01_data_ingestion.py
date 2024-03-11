from TextSummarizer.components.data_ingestion import DataIngestion
from TextSummarizer.config.configuration import ConfigurationManager
# from TextSummarizer.logging.logger import logger

class DataIngestionTrainingpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_filepath = "config.yaml"
        params_filepath = "params.yaml"
        
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()
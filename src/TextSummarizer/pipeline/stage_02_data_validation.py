from TextSummarizer.components.data_validation import Datavalidation
from TextSummarizer.config.configuration import ConfigurationManager
# from TextSummarizer.logging.logger import logger

class DataValidationTrainingpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_ingestion = Datavalidation(config = data_validation_config)
        data_ingestion.validate_all_files_exist()

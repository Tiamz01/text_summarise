from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging.logger import logger

class DataTransformationTrainingpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()
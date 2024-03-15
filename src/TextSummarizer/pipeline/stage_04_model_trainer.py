from TextSummarizer.components.Model_trainer import ModelTrainer
from TextSummarizer.config.configuration import ConfigurationManager
# from TextSummarizer.logging.logger import logger

class ModelTrainingpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_filepath = "config.yaml"
        params_filepath = "params.yaml"

        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
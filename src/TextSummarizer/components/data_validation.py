import os
from TextSummarizer.entity.entity import DataValidationConfig
from TextSummarizer.logging.logger import logger



# data validation components
class Datavalidation:
    """
    This class contains the methods for validating the data.
    """

    def __init__(self, config: DataValidationConfig):
        """
        Initialize the class with the configuration.

        Args:
            config (DataValidationConfig): The configuration for the data validation.
        """
        self.config = config

    def validate_all_files_exist(self) -> bool:
        """
        Validate if all the required files exist.

        Returns:
            bool: True if all the required files exist, False otherwise.
        """
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILE:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e

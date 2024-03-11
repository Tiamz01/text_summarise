from TextSummarizer.logging.logger import logger
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingpipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingpipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<<<<")
    data_Ingestion = DataIngestionTrainingpipeline()
    data_Ingestion.main()
    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<<<<")
    data_Validation = DataValidationTrainingpipeline()
    data_Validation.main()
    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
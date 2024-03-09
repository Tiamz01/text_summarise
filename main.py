from TextSummarizer.logging.logger import logger
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingpipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<<<<")
    data_Ingestion = DataIngestionTrainingpipeline()
    data_Ingestion.main()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import (DataIngestionTrainingPipeline)
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME='Data Ingestion Stage'

try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<<<\n\nx========x")
    obj=DataIngestionTrainingPipeline()
    obj.intiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Data Validation Stage'

try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<<<\n\nx========x")
    obj=DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e
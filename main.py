from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import (DataIngestionTrainingPipeline)
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_training_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

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

STAGE_NAME='Data Transformation Stage'

try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<<<\n\nx========x")
    obj=DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Training Stage'

try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<<<\n\nx========x")
    obj=ModelTrainerTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Evaluation Stage'

try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<<<\n\nx========x")
    obj=ModelEvaluationTrainingPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e
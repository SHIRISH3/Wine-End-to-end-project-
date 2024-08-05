from wine_quality_project import logger
from wine_quality_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wine_quality_project.pipeline.stage_02_data_validation import DataValidationTrainingPipline
from wine_quality_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<<")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<< \n \nX===========================X")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME= "Data Validation Stage"
try:
    logger.info(f">>>>>stage {STAGE_NAME} started")
    obj= DataValidationTrainingPipline()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<< \n \n x=================x")
except Exception as e:
    logger.exception()
    raise 

STAGE_NAME= "Data Transformation Stage"
try:
    logger.info(f">>>>>stage {STAGE_NAME} started")
    data_ingestion= DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<< \n \n x=================x")
except Exception as e:
    logger.exception(e)
    raise e
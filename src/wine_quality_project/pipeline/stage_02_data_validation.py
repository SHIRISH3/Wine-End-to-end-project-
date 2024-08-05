from wine_quality_project.config.configuration import ConfigurationManager
from wine_quality_project.components.data_validation import DataValidation
from wine_quality_project import logger

STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipline:
    def __init__(self):
        pass

    def main(Self):
        config= ConfigurationManager()
        data_validation_config= config.get_data_validation_config()
        data_validation= DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__=='__main__':
    try:
        logger.info(f">>>>>stage {STAGE_NAME} started")
        obj= DataValidationTrainingPipline()
        obj.main()
        logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<< \n \n x=================x")
    except Exception as e:
        logger.exception()
        raise e
    
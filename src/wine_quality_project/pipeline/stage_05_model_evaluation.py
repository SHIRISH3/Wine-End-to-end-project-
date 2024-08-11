from wine_quality_project.config.configuration  import ConfigurationManager
from wine_quality_project.components.model_evaluation import ModelEvaluation
from wine_quality_project import logger

STAGE_NAME= "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config= ConfigurationManager()
        model_evealuation_config= config.get_model_evaluation_config()
        model_evealuation_config= ModelEvaluation(config= model_evealuation_config)
        model_evealuation_config.save_results()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj= ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\n X================x")
    except Exception as e:
        logger.exception(e)
        raise e
    
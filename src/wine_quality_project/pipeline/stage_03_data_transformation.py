from wine_quality_project.config.configuration import ConfigurationManager
from wine_quality_project.components.data_transformation import DataTransformation
from wine_quality_project import logger
from pathlib import Path

STAGE_NAME= "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(Self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status= f.read().split(" ")[-1]
            
            if status== "True":
                config= ConfigurationManager()
                Data_transformation_config= config.get_data_transformation_config()
                Data_transformation=  DataTransformation(config= Data_transformation_config)
                Data_transformation.train_test_split()

            else:
                raise Exception("Your data schema is not valid")
        
        except Exception as e :
            print(e)
            

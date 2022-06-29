from housing.entity.config_entity import ModelEvaluationConfig,ModelEvaluationArtifact
import sys,os
from housing.exception import HousingException
from housing.logger import logging

class ModelEvaluation:

    def __init__(self,model_evaluation_config:ModelEvaluationConfig ):
        try:
            logging.info(f"{'='*20}Model Evaluation log started.{'='*20} ")
            self.model_evaluation_config = model_evaluation_config
        except Exception as e:
            raise HousingException(e,sys)


    def initiate_model_Evaluation(self)-> ModelEvaluationArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
from housing.entity.config_entity import ModelTrainerConfig,ModelTrainerArtifact
import sys,os
from housing.exception import HousingException
from housing.logger import logging

class ModelTrainer:

    def __init__(self,model_trainer_config:ModelTrainerConfig ):
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20} ")
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise HousingException(e,sys)


    def initiate_model_trainer(self)-> ModelTrainerArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
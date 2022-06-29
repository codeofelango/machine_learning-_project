from housing.entity.config_entity import ModelPusherConfig,ModelPusherArtifact
import sys,os
from housing.exception import HousingException
from housing.logger import logging

class ModelPusher:

    def __init__(self,model_pusher_config:ModelPusherConfig ):
        try:
            logging.info(f"{'='*20}Model Pusher log started.{'='*20} ")
            self.model_pusher_config = model_pusher_config
        except Exception as e:
            raise HousingException(e,sys)


    def initiate_model_pusher(self)-> ModelPusherArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
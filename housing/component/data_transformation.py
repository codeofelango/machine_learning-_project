from housing.entity.config_entity import DataTransformationConfig,DataTransformationArtifact
import sys,os
from housing.exception import HousingException
from housing.logger import logging

class DataTransformation:

    def __init__(self,data_transformtion_config:DataTransformationConfig ):
        try:
            logging.info(f"{'='*20}Data Tranformation log started.{'='*20} ")
            self.data_transformtion_config = data_transformtion_config
        except Exception as e:
            raise HousingException(e,sys)


    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
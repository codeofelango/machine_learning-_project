from housing.entity.config_entity import DataValidationConfig,DataValidationArtifact
import sys,os
from housing.exception import HousingException
from housing.logger import logging

class DataValidation:

    def __init__(self,data_validation_config:DataValidationConfig ):
        try:
            logging.info(f"{'='*20}Data Tranformation log started.{'='*20} ")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise HousingException(e,sys)


    def initiate_data_transformation(self)-> DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
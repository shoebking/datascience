import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataTransformationConfig)
from sklearn.model_selection import train_test_split # type: ignore
import pandas as pd

## component-Data Ingestion

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
    
    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

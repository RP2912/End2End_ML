# read the dataset from data source and split the data, and transform

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from  sklearn.model_selection import train_test_split
from dataclasses import dataclass

# save the test data and train data and raw data, these inputs

@dataclass #nt req init , cn directly define class variable using decortr

class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv') #saving data in artifacts and these are the inputs giving to dataingestion

class DataIngestion:
    def __init__(self): #if defining jus variable use @dataclass , if there are other functions use __init__
        self.ingestion_config=DataIngestionConfig() #when call above 3 inputs will save in ingestion_config

    def initiate_data_ingestion(self): # use to read the data from data surce
        logging.info("entered the data ingestion method")
        try:
            df=pd.read_csv(r'D:\Data science\Projects\End2End_ML\notebook\data.csv')
            logging.info('Read the dataset as dataframe')#keep writing logginf .info so to get where exception happens
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("train test spit initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True) #saving afeter train test split

            logging.info("ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()




import sys
import pandas as pd
import os
sys.path.insert(0, os.curdir)
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from logger import logging
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw_data.csv")
    test_data_path:str = os.path.join("artifacts","test_data.csv")
    train_data_path:str = os.path.join("artifacts","train_data.csv")
    

class DataIngestion:
    def __init__(self):
        self.DataIngestionConfigObj = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Initiating Data Injection")
            df=pd.read_csv('notebook/data/Stud.csv')

            logging.info("Dataframe is created successfully")
            os.makedirs(os.path.dirname(self.DataIngestionConfigObj.raw_data_path),exist_ok=True)
            df.to_csv(self.DataIngestionConfigObj.raw_data_path,index=False,header=True)
            logging.info("Raw data file is saved in Artifact location")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
        
            os.makedirs(os.path.dirname(self.DataIngestionConfigObj.train_data_path),exist_ok=True)

            train_set.to_csv(self.DataIngestionConfigObj.train_data_path,index=False,header=True)
            logging.info("Train data file is saved in Artifacts folder")

            os.makedirs(os.path.dirname(self.DataIngestionConfigObj.test_data_path),exist_ok=True)

            test_set.to_csv(self.DataIngestionConfigObj.test_data_path,index=False,header=True)
            logging.info("Test data file is saved in Artifacts folder")

            return(
                self.DataIngestionConfigObj.test_data_path,
                self.DataIngestionConfigObj.test_data_path
                )
        except Exception as e:
                 CustomException(e,sys)
                 logging.info("Error while initiate the Data Ingestion"+e)


if __name__=='__main__':
     obj=DataIngestion()
     obj.initiate_data_ingestion()

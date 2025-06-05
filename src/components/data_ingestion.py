# All tasks that invlve reading the data
import os
import sys

# We do this as we will be using our custom exception
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

'''
There are inputs required by the data ingestion like saving train data, test data, raw data
This will we done in a separate class
Any input required by data_ingestion will be passed via this
Now to define class variable we use init. However, if we use decorator dataclass we can directly define class variable
'''

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv") # We are giving this input to data ingestion, a path where data ingestion will save all the output
    # So training data will be saved in a folder called artifacts in a train.csv file
    test_data_path: str = os.path.join('artifacts', "test.csv" )
    raw_data_path: str = os.path.join('artifacts', "data.csv" )

# So we gave input of path and we get the file as output

'''
If you are defining only variable then use dataclass otherwise if there are functions in the class then use init
'''
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # Here we are initialising these inputs

    def initiate_data_ingestion(self):
        ''' 
        Write code to read data from a database.
        We can create a MongoDB or SQL client in utils and then read it.
        Here we are doing it in easy way. But later we can do the above. 
        '''

        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(r'notbook\data\stud.csv') # We can also directly read over here from mongo db and sql by just changing this part. NOTHING ELSE.
            logging.info('Read the dataset as data frame')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            df.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True) # Saving the split into artifact folder
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            logging.info("Ingestion of data is completed")

            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path) # This info is required by the data transformation which it can directly take from here
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
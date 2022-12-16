import pandas as pd 
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    This function return collection as dataframe
    database_name : database name
    """
    
    try:
        logging.info(f"reading data from database")
        df = DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Columns : {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping Column : _id")
            df = df.drop("_id",axis = 1)
        logging.info(f"Row and Columns in df : {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e,sys)
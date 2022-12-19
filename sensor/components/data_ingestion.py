from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging

class DataIngestion:
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(Self)->artifact_entity.DataIngestionArtifact():
        try:
            # Exporting collection data as pandas dataframe
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name = self.data_ingestion_config.database_name, 
                collection_name = self.data_ingestion_config.collection_name)
            # save data in feature store
            df.replace(to_replace = "na",value=np.NAN,inplace = true)

            #create feature store folder
            feature_store_dir = os.path.dirname(Self,data_ingestion_config.feature_store_file_path,index=False,header=True)

            logging.info("split this dataset into train and test set")

            # split dataset into train and test set
            train_df,test_df =  train_test_split(df,test_size=self.data_ingestion_config.test_size)
        except Exception as e:
            raise SensorException(e, sys)

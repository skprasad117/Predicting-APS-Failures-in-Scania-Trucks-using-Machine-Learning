import pymongo
import pandas as pd
import json 

from sensor.config import mongo_client
# Provide the mongodb localhost url to connect python to mongodb


DATA_FILE_PATH = "aps_failure_training_set1.csv"
# Database Name
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns:{df.shape}")

    # convert dataframe to json
    # dropping the index
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    # insert command to mongoDB
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

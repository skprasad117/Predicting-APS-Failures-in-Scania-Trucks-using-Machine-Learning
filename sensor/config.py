import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://sanjay:password@cluster0.m69g2.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "aps_failure_training_set1.csv"
# Database Name
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

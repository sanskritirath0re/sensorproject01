from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://sanskriti:12345@cluster0.b4gmo.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to server
client=MongoClient(uri)

#create a database and collection
DATABASE_NAME="sans"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\sansk\OneDrive\Desktop\Sensor project\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
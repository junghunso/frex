import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb+srv://jungso:post9169@cluster0.kbds79b.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

db.fc_list.drop()

df1 = pd.DataFrame.from_records(db.fc_list_update.find({}, {'_id': False}))

db.fc_list.insert_many(df1.to_dict('records'))


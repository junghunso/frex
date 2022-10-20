import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb+srv://jungso:post9169@cluster0.kbds79b.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

db.fc_update.drop()

df1 = pd.DataFrame.from_records(db.fc_list_update.find({}, {'_id': False}))
df2 = pd.DataFrame.from_records(db.fc_list.find({}, {'_id': False}))

df1['z_u1'] = df1['상호'] + df1['영업표지']
df2['z_u1'] = df2['상호'] + df2['영업표지']
df1['z_key1'] = df1['z']
df2['z_key2'] = df2['z']

df3 = pd.merge(df1, df2, how='outer', on='z_u1')
cond1 = (df3['z_key2'].isnull())

df4 = df3[cond1]

z = df4['z_key1'].to_list()

for d in z:
    doc = {
        'z': d,
    }
    db.fc_update.insert_one(doc)

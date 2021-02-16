from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
MONGODB_URI=os.environ['MONGO_URI']
client=MongoClient(MONGODB_URI)

for db_info in client.list_database_names():
    print(db_info)

db=client['sample']

colls=db.list_collection_names()
for coll in colls:
    print("collection \n" + coll)

from pprint import pprint

cat=db['DataList']
pprint(cat.find_one({'name':'oko'}))

# insert/ create     / save

insert_cat=cat.insert_one({
    'name': 'newpy',
    'desc': 'z py',
    'number':45
})

new_id=insert_cat.inserted_id

# read all

import bson
print(cat.find_one({ '_id': bson.ObjectId(new_id)}))

print("ALL inserted \n" )
for x in cat.find():
    pprint(x)

pprint(cat.count_documents({}))


# cat.delete_many({})
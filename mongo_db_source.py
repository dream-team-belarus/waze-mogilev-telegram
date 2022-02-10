import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
uri = os.getenv('DB_CONF')
cluster = MongoClient(uri)
db = cluster['source']
places = db['places']
actions = db['actions']

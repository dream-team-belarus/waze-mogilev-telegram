import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()


cluster = pymongo.MongoClient(f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/?retryWrites=true&w=majority")




db = cluster['source']
places = db['places']
actions = db['actions']

import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

cluster = pymongo.MongoClient(f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/?retryWrites=true&w=majority")

db = cluster['telega']
full_story = db['fullstory']
wrong_place = db['wrongplace']
wrong_action = db['wrongaction']
wrong_position = db['wrongposition']
wrong_something = db['wrongsomething']
success = db['success']
success_history = db['success_history']
drop = db['drop']

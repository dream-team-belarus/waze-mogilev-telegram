import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
uri = os.getenv('DB_CONF')
cluster = MongoClient(uri)
db = cluster['telega']
full_story = db['fullstory']
wrong_place = db['wrongplace']
wrong_action = db['wrongaction']
wrong_position = db['wrongposition']
wrong_something = db['wrongsomething']
success = db['success']
success_history = db['success_history']
drop = db['drop']

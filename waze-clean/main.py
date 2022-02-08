from pymongo import MongoClient
from datetime import datetime, timedelta
import time
import requests
import re
import schedule
import os
from dotenv import load_dotenv


load_dotenv()

def remove_event_from_feed():
  uri = os.getenv('DB_CONF')
  cluster = MongoClient(uri)
  db = cluster['telega']
  success = db['success']
  time_zone = datetime.now() + timedelta(hours=3)
  doc = success.find_one({'remove': {'$lt': time_zone}}, {"feed_id": 1})
  result = str(set(re.findall(r"\W\d{5}\W", str(doc))))
  feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
  if not feed_id:
    print('nothing to do')
  else:
    s = requests.session()
    payload = {
      'LoginForm[username]': os.getenv("FEED_CLEAN_LOGIN"),
      'LoginForm[password]': os.getenv("FEED_CLEAN_PASSWORD"),
    }
    s.post("https://feed.waze.su/ru/site/login/*", data=payload)
    s.post('https://feed.waze.su/ru/feed/delete/*?id=' + feed_id)
    success.delete_one({"feed_id": feed_id})
    print(feed_id + ' was delete')


schedule.every(2).minutes.do(remove_event_from_feed)


while True:
    schedule.run_pending()
    time.sleep(1)

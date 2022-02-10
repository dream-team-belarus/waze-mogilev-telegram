from datetime import datetime, timedelta
import mongo_db_script
import mongo_db_source
from telethon import TelegramClient, events, sync
import requests
import os
import re
from dotenv import load_dotenv


load_dotenv()
client = TelegramClient('waze_belarus', os.getenv("API_ID"), os.getenv("API_HASH"))
client.start()
client.send_message('alexeyryabtsev', '🚔')


@client.on(events.NewMessage(pattern=r'(?i).*\b()\b'))
async def handler(event):
  t_ve_time = datetime.now() + timedelta(hours=3, minutes=0, seconds=5)
  live_time = t_ve_time.strftime("%y-%m-%dT%H:%M:%S")
  t_fe_time = t_ve_time + timedelta(minutes=30)
  life_time = t_fe_time.strftime("%y-%m-%dT%H:%M:%S")
  message_low = event.text.lower()
  arr = ["!", ".", "-", "?", ",", "🚔", "+"]
  for x in arr:
    message_low = message_low.replace(x, "")
  message_split = message_low.split(' ')
  #
  for i in message_split:
    drop_search = mongo_db_source.actions.find({"drop": i}, {"drop":1})
    police_search = mongo_db_source.actions.find({"police": i}, {"police":1})
    accident_search = mongo_db_source.actions.find({"accident": i}, {"accident":1})
    help_search = mongo_db_source.actions.find({"help": i}, {"help":1})
    for i in drop_search:
      if i:
        print(event.text,' dropped')
        break
    for i in police_search:
      if i:
        action="POLICE"
        subtype="POLICE_VISIBLE"
        caterpilar(event, life_time, live_time, message_low, message_split, t_fe_time, action, subtype)
        break
    for i in accident_search:
      if i:
        action="accident"
        subtype="ACCIDENT_MINOR"
        caterpilar(event, life_time, live_time, message_low, message_split, t_fe_time, action, subtype)
        break
    for i in help_search:
      if i:
        print(event.text,' dropped. Temporary help is not support')
        break


def successful_action(feed_id, live_time, event, message_split, t_fe_time):
    mongo_db_script.success.insert_one(
            {"feed_id": feed_id, "feed_time": live_time, "message": event.text,
             "fabrika": message_split, "remove": t_fe_time})
    #mongo_db_script.success_history.insert_one({"_id": live_time, "message": event.text})
    print('success ', live_time, ' ', event.text, ' ', feed_id)
    print('---')


def wrong_action(event, live_time, message_split):
    print('wrong place')
    mongo_db_script.wrong_place.insert_one({"feed_time": live_time, "message": event.text, "fabrika": message_split})


def caterpilar(event, life_time, live_time, message_low, message_split, t_fe_time, action, subtype):
  for i in message_split:
    place_search = mongo_db_source.places.find({"place": i},{"coordinate": 1, "place": 1})
    for i in place_search:
      if i:
        message_split = message_low.split(" ")
        s = requests.session()
        payload = {
          'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
          'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
          'Feed[polyline]': i['coordinate'],
          'Feed[starttime]': live_time,
          'Feed[endtime]': life_time,
          'Feed[direction]': 'BOTH_DIRECTIONS',
          'Feed[type]': action,
          'Feed[subtype]': subtype,
          'Feed[description]': 'ДТП и ЧП Могилев',
          'Feed[comment]': message_low,
          'Feed[street]': 'Могилев',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)
        break
      return feed_id


client.run_until_disconnected()

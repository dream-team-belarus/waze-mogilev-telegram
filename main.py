from datetime import datetime, timedelta
import mongo_db_script
import mongo_db_source
from telethon import TelegramClient, events, sync
import requests
import os
import re
import pymongo
from dotenv import load_dotenv


load_dotenv()
client = TelegramClient('waze_belarus', os.getenv("API_ID"), os.getenv("API_HASH"))
client.start()
client.send_message('alexeyryabtsev', '🚔')


@client.on(events.NewMessage(pattern=r"(?i).*\b()\b"))
async def handler(event):
  t_ve_time = datetime.now() + timedelta(hours=3, minutes=0, seconds=5)
  live_time = t_ve_time.strftime("%y-%m-%dT%H:%M:%S")
  t_fe_time = t_ve_time + timedelta(minutes=30)
  life_time = t_fe_time.strftime("%y-%m-%dT%H:%M:%S")
  message_low = event.text.lower()
  arr = ['!', '.', '-', '?', ',', '🚔', '+', '"']
  for x in arr:
    message_low = message_low.replace(x, " ")
  message_split = message_low.split(' ')
  print("----------------------------")
  print(event.text)

  
  action = "empty"

  for i in message_split:
    while action == "empty":
      search = mongo_db_source.actions.find({'words': i})
      for a in search:
        if a["action"] == "drop":
          action = "drop"
        elif a["action"] == "police":
          action = "police"
      break
  print("action: ", action)
  #------------------------------------------------------------

  place = "empty"

  for i in message_split:
    while place == "empty":
      search = mongo_db_source.places.find({'place': i})
      for a in search:
        if a["_id"] != 0:
          place = a["_id"]
      break
  print("place : ", place)

  #============================================================
  
  checker(action, place, event, live_time, t_fe_time)

def checker (action, place, event, live_time, t_fe_time):
  if action == "drop":
    print("Usual message without any info")
  elif action == "empty":
    print("I don't know this action, so let's check")
    mongo_db_script.wrong_action.insert_one({"message": event.text})
    print("message added to base wrong actions for research")
  elif place == "empty":
    print("I don't know this place, so let's check")
    mongo_db_script.wrong_place.insert_one({"message": event.text})
    print("message added to base wrong places for research")
  else:
    print("SUCCESS, move to database")
    mongo_db_script.success.insert_one({"time": live_time, "message": event.text, "remove": t_fe_time})

client.run_until_disconnected()

from datetime import datetime, timedelta
import places
import mongo_db_script
from telethon import TelegramClient, events, sync
import olimpiada
import requests
import os
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
  # отметаем всякий мусор типа спасибо
  x = []
  for a in message_split:
    for b in olimpiada.drops:
      if a == b:
        x.append(a)
        break
  y = []
  for a in message_split:
    for b in olimpiada.actions:
      if a == b:
        y.append(a)
        break
  z = []
  for a in message_split:
    for b in olimpiada.dtp_act:
      if a == b:
        z.append(a)
        break
  if len(x) >= 1:
    drop(event, live_time, message_split, t_fe_time)
  elif len(z) >= 1:
    dtp(event, life_time, live_time, message_low, message_split, t_fe_time)
  elif len(y) >= 1:
    police(event, life_time, live_time, message_low, message_split, t_fe_time)
  return life_time, live_time, message_split, t_fe_time


def police(event, life_time, live_time, message_low, message_split, t_fe_time):
  for i in range(len(olimpiada.position)):
      for a in olimpiada.position[i]:
        if a in message_split:
          for b in olimpiada.actions:
            if b in message_split:
              places.place[i](event, live_time, life_time, message_low, t_fe_time)
              break


def dtp(event, life_time, live_time, message_low, message_split, t_fe_time):
  for i in range(len(olimpiada.position)):
      for a in olimpiada.position[i]:
        if a in message_split:
          for b in olimpiada.dtp_act:
            if b in message_split:
              places.place[i](event, live_time, life_time, message_low, t_fe_time)
              break


def drop(event, live_time, message_split, t_fe_time):
  '''mongo_db_script.drop.insert_one({"feed_time": live_time, "message": event.text, "fabrika": message_split})'''
  print('dropped', message_split)


def wrong_action(event, live_time, message_split):
  mongo_db_script.wrong_action.insert_one({"feed_time": live_time, "message": event.text, "fabrika": message_split})
  print('wrong action')


def wrong_position(event, live_time, message_split):
  mongo_db_script.wrong_position.insert_one({"feed_time": live_time, "message": event.text, "fabrika": message_split})
  print('wrong position')


def wrong_something(event, live_time, message_split):
  mongo_db_script.wrong_something.insert_one({"feed_time": live_time, "message": event.text, "fabrika": message_split})
  print('unknown place or action')


client.run_until_disconnected()

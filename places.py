import mongo_db_script
import requests
import olimpiada
import re
import os
from dotenv import load_dotenv


load_dotenv()
def place00():
    print('next')


'''
def remove_event_from_feed(feed_id):
    s = requests.session()
    payload = {
        'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
        'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
    }
    s.post("https://feed.waze.su/ru/site/login/*", data=payload)
    s.post('https://feed.waze.su/ru/feed/index/*?FeedSearch%5Bid%5D=' + feed_id + '&FeedSearch%5BauthorFilterInput%5D=ry&FeedSearch%5Bdescription%5D=&FeedSearch%5Bcreated_at%5D=&FeedSearch%5Bstarttime%5D=&FeedSearch%5Bendtime%5D=&FeedSearch%5Bstreet%5D=&FeedSearch%5Btype%5D=&FeedSearch%5Bsubtype%5D=&FeedSearch%5Bdirection%5D=&FeedSearch%5Bcomment%5D=&_pjax=%23p0')
    s.post('https://feed.waze.su/ru/feed/delete/*?id=' + feed_id)

def print_feed_id(feed_id):
    print(feed_id)
'''
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


def place01(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.909470 30.361668',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH_EAST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Королёва',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place02(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.928428 30.338827',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'NORTH',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Первомайская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place03(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.879737 30.410495',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'шоссе Чаусское',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place04(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.867021 30.362854',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Димитрова',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place05(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.915482 30.341890',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Первомайская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place06(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.897070 30.333092',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Болдина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place07(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.912452 30.317718',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH_WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Космонавтов',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place08(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.917394 30.374593',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Мира',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place09(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.923131 30.368794',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Гришина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place10(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.845940 30.336500',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Шмидта',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place11(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.862859 30.358333',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'шоссе Гомельское',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place12(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.982284 30.317542',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-76',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place13(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.829566 30.671073',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-122',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place14(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.956643 30.205792',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'NORTH_WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-4',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place15(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.972990 30.135221',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'EAST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-4',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place16(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.902944 30.336564',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Первомайская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place17(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.898291 30.331929',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Лазаренко',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place18(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.899290 30.333683',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Первомайская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place19(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.899954 30.296835',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'NORTH_EAST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Космонавтов',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place20(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.927724 30.348612',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Гришина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place21(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.968364 30.349460',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': ' ',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place22(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.917861 30.309023',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Якубовского',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place23(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.855680 30.255416',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': ' ',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place24(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.868256 30.327271',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH_EAST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Шмидта',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place25(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.957393 30.467548',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place26(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.881919 30.403413',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Витебский',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place27(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.884218 30.336681',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Большая Чаусская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place28(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.877454 30.265506',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Челюскинцев',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place29(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.886431 30.254547',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Шоссейная',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place30(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.883533 30.326909',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Гагарина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place31(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.875415 30.316597',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH_EAST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Шмидта',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place32(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.867404 30.475149',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-122',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place33(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.911975 30.346502',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'NORTH',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Ленинская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place34(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.951254 30.360176',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH_WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Крупской',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place35(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '54.117328 30.458291',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Локути',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place36(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.853171 30.545056',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-122',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place37(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.793031 30.196558',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': ' ',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place38(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '54.186394 30.308719',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-76',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place39(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.874523 30.312356',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Симонова',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place40(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.785584 30.187077',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-93',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place41(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.896031 30.466609',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Лесничество',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place42(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.908529 30.356590',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'EAST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Мира',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place43(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.906899 30.364508',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'NORTH_WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Королёва',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place44(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '54.035424 30.323973',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': ' ',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place45(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.916286 30.316280',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Якубовского',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place46(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.840507 30.248393',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-93',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place47(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.865389 30.356399',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Пушкинский',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place48(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.928030 30.361967',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица 30 лет Победы',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place49(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.919695 30.291940',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Загородное шоссе',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id

def place50(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.914258 30.380126',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Гришина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place51(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.906342 30.341837',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Миронова',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place52(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.908113 30.312540',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'NORTH_WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Лазаренко',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place53(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.978643 30.466407',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place54(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.911803 30.339045',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Тимирязевская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place55(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.912667 30.365334',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Мира',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place56(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.904840 30.338026',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'NORTH',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Первомайская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place57(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.905325 30.336647',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Яцыно',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place58(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.868896 30.349860',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH_WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Габровская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place59(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.905162 30.344039',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Миронова',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place60(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.860045 30.324976',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Симонова',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place61(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '54.395282 30.443021',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place62(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '54.142294 30.317248',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-76',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place63(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.897874 30.338341',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'переулок Пожарный',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place64(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.978818 30.033123',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-4',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place65(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.266299 29.472471',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Гагарина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place66(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.775695 30.363980',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': ' ',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place67(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.815347 30.449682',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-71',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place68(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.880954 30.145612',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Шоссейная',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place69(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.909563 30.309489',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Лазаренко',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place70(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.905813 30.344782',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Ленинская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place71(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.810654 30.361697',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': ' ',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place72(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.863417 30.258984',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'H-93',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place73(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.887043 30.331500',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH_EAST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Пушкинский',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place74(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.878138 30.338903',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Островского',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place75(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.967090 30.168647',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': ' ',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id

    
def place76(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.881607 30.357103',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Терехина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place77(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.960500 30.360712',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Крупской',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place78(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.707484 30.085990',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-93',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place79(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.530650 30.343083',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place80(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.571584 30.338570',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place81(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.604216 30.345329',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place82(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.683868 30.369738',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place83(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.680433 30.673241',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place84(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.911475 30.343603',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Тимирязевская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place85(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.927391 30.353039',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Гришина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place86(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.838887 30.396802',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'шоссе Славгородское',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place87(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.803145 30.257796',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Шоссейная',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 

    
def place88(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.797018 30.498682',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Быстрик',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place89(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.790639 30.524753',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-71',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place90(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '54.146313 30.456571',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place91(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '54.283656 30.449074',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'М-8',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place92(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.155905 30.460838',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Гомельская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place93(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.75776, 30.36502',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': ' ',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place94(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.881151 30.335852',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Пушкинский',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place95(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.879830 30.338196',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Чигринова',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 
    

def place96(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.873369 30.310505',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Кутепова',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 
    

def place97(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.916423 30.296579',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Алексея Пысина',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place98(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.937946 30.241959',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Льва Сапеги',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 

    
def place99(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.932318 30.243906',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Тишки Гартного',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 

    
def place100(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.908065 30.351237',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'проспект Мира',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place101(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.902941 30.336045',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'переулок Тани Карпинской',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 

    
def place102(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.906789 30.292860',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Строителей',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place103(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.876565 30.335555',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Чайковского',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place104(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.893796 30.313650',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Челюскинцев',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id 


def place105(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.894798 30.322157',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Быховская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place106(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.864591 30.378901',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Павлова',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id  

    
def place107(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.887807 30.265294',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'улица Вишневецкого',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id      
    
     
def place108(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.883093 30.407334',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'рынок Любужский',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id  
       
     
def place109(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.792044 31.004938',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Р-122',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id  
      
     
def place110(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.909357 30.333678',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'WEST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Дом Спорта',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id  


def place111(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.910858 30.326157',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Дворец пионеров',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id  


def place112(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.944161 30.232938',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'SOUTH_EAST',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Присно',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id  


def place113(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.870802 30.458332',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Большая Боровка',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id  
    

def place114(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.871691 30.433511',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Малая Боровка',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place115(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.911062 30.283741',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Сентябрьский мост',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id   


def place116(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.872401 30.358094',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Ома',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id    


def place117(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.884035 30.414396',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Торпедо',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)        
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place118(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.dtp_act:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.914295 30.316858',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'ACCIDENT',
            'Feed[subtype]': 'ACCIDENT_MINOR',
            'Feed[description]': 'DTP',
            'Feed[comment]': message_low,
            'Feed[street]': 'Якубовского',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place119(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.dtp_act:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.893582 30.330745',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'ACCIDENT',
            'Feed[subtype]': 'ACCIDENT_MINOR',
            'Feed[description]': 'DTP',
            'Feed[comment]': message_low,
            'Feed[street]': 'Орджоникидзе',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place120(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.833078 30.379770',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Вейно',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


def place121(event, live_time, life_time, message_low, t_fe_time):
    message_split = message_low.split(" ")
    c = []
    for a in message_split:
        for b in olimpiada.actions:
            if a == b:
                c.append(a)
                break
    if len(c) >= 1:
        s = requests.session()
        payload = {
            'LoginForm[username]': os.getenv("FEED_MAIN_LOGIN"),
            'LoginForm[password]': os.getenv("FEED_MAIN_PASSWORD"),
        }
        s.post("https://feed.waze.su/ru/site/login/*", data=payload)
        batch = {
            'Feed[polyline]': '53.938538 30.340236',
            'Feed[starttime]': live_time,
            'Feed[endtime]': life_time,
            'Feed[direction]': 'BOTH_DIRECTIONS',
            'Feed[type]': 'POLICE',
            'Feed[subtype]': 'POLICE_VISIBLE',
            'Feed[description]': 'police',
            'Feed[comment]': message_low,
            'Feed[street]': 'Актюбинская',
        }
        response = s.post("https://feed.waze.su/ru/feed/create/*", data=batch)
        result = str(set(re.findall(r"\b\w+\b=\d{5}", str(response.content))))
        feed_id = str(set(re.findall(r"\d{5}", result)))[2:7]
        successful_action(feed_id, live_time, event, message_split, t_fe_time)
    else:
        wrong_action(event, live_time, message_split)
    return feed_id


place = [place00, place01, place02, place03, place04, place05, place06, place07, place08, place09,
         place10, place11, place12, place13, place14, place15, place16, place17, place18, place19,
         place20, place21, place22, place23, place24, place25, place26, place27, place28, place29,
         place30, place31, place32, place33, place34, place35, place36, place37, place38, place39,
         place40, place41, place42, place43, place44, place45, place46, place47, place48, place49,
         place50, place51, place52, place53, place54, place55, place56, place57, place58, place59,
         place60, place61, place62, place63, place64, place65, place66, place67, place68, place69,
         place70, place71, place72, place73, place74, place75, place76, place77, place78, place79,
         place80, place81, place82, place83, place84, place85, place86, place87, place88, place89,
         place90, place91, place92, place93, place94, place95, place96, place97, place98, place99,
         place100, place101, place102, place103, place104, place105, place106, place107, place108, place109,
         place110, place111, place112, place113, place114, place115, place116, place117, place118, place119,
         place120, place121, '''place122, place123, place124, place125, place126, place127, place128, place129,'''
         ]
         
         

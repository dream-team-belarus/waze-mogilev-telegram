FROM python:3.9

WORKDIR /home

RUN apt-get update
RUN pip install datetime pymongo telethon dnspython requests python-dotenv

COPY .env ./
COPY *.py ./
COPY *.session ./
COPY __pycache__ ./

ENTRYPOINT ["python", "main.py"]

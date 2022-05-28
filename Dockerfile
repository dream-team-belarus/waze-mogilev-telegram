FROM python:3.9

WORKDIR /home

RUN apt-get update
RUN pip install datetime pymongo telethon dnspython requests python-dotenv

COPY *.py ./
COPY *.session ./

ENTRYPOINT ["python", "main.py"]

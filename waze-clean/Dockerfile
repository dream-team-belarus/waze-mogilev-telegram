FROM python:3.9

WORKDIR /home

RUN apt-get update
RUN pip install datetime pymongo dnspython requests schedule python-dotenv

COPY main.py ./

ENTRYPOINT ["python", "main.py"]

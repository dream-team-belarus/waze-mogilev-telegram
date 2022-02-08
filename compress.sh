#!/bin/bash

ZIP_FILE="./waze-mogilev.zip"

zip -r $ZIP_FILE \
    ./.env \
    ./*.py \
    ./waze-clean \
    ./Dockerfile \
    ./__pycache__.zip \
    ./docker-compose.yml \


#!/bin/bash

ZIP_FILE="./waze-mogilev.zip"

zip -r $ZIP_FILE \
    ./.env \
    ./*.py \
    ./waze-clean \
    ./Dockerfile \
    ./*.session \
    ./docker-compose.yml \

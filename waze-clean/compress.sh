#!/bin/bash

ZIP_FILE="./waze-mogilev-clean.zip"

zip -r $ZIP_FILE \
    ./main.py \
    ./Dockerfile \

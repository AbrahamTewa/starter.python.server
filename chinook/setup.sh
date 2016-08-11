#!/usr/bin/env sh

apk update
apk add gcc postgresql-dev musl-dev
pip install -r requirements.txt
python manage.py migrate

#!/bin/sh

bash ./wait-for-it.sh postgres:5432 -t 30
python3 manage.py migrate
celery worker --app=web_task -c 2 & python3 manage.py runserver 0.0.0.0:8000

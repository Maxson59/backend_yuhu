#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py migrate

gunicorn -b 0.0.0.0:$PORT -w 4 --threads 2 app.wsgi
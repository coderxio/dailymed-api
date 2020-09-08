#!/bin/bash
python /dailymed-api/api/manage.py migrate
exec /dailymed-api/api/manage.py runserver 0.0.0.0:8000

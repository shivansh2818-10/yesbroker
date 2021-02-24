@echo off
color 0a
title YES BROKER SERVER
cls
start http://localhost:8000
python manage.py runserver
@echo off
pip install --upgrade pip
pip install -r requirements.txt
pyhthon manage.py makemigrations
python manage.py migrate
python manage.py runserver
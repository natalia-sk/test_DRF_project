# study-time

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Local Setup](#local-setup)

## General info
The project is an educational platform with two types of content: a video course (with episodes) and an article. The platform also includes in-app notifications about new content.
	
## Technologies
Project is created with:
* Python 3.7.11
* Django 3.2.6
* Django Rest Framework 3.12.4
* django-filter 2.4.0
* drf-extensions 0.7.1
	
## Local Setup
1) Create virtual environment  
`virtualenv -p python3 venv`  
2) Activate created virtual environment  
`. venv/bin/activate`
3) Install requirements  
`pip3 install -r requirements.txt`
4) Run migrations  
`python manage.py migrate`
5) Create an admin user  
`python manage.py createsuperuser`

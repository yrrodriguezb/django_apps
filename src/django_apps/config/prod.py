from os import environ
from .base import *


DEBUG = False

THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = [ 'yrrodriguezb.com', ]

# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_apps',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = environ.get("DJANGO_EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = environ.get("DJANGO_EMAIL_HOST_PASSWORD", None)
EMAIL_PORT = '2525'
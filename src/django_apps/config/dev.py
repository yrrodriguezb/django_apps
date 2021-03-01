from .base import *


DEBUG = True

ALLOWED_HOSTS = []

# Database

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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
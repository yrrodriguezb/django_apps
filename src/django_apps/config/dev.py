from .base import *


DEBUG = True

ALLOWED_HOSTS = []

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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

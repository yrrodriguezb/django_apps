from .base import *


DEBUG = True

ALLOWED_HOSTS = [ 'yrrodriguezb.com', 'localhost', '127.0.0.1' ]

# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
from .base import *


DEBUG = False

ALLOWED_HOSTS = ['localhost', ]

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yoorusername@gmail.com'
EMAIL_HOST_PASSWORD = 'key' 
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'
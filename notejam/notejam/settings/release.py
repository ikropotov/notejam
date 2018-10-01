from base import *
import os

# Disable debug
if os.environ.get('DEBUG'):
    DEBUG = True
else:
    DEBUG = False

# Must be explicitly specified when Debug is disabled
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'notejamdb'),
        'USER': os.environ.get('MYSQL_USER', 'notejam'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'password'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
    }
}

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/www/notejam/static')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/var/www/notejam/media')
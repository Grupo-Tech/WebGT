from .base import *

IS_HEROKU = "DYNO" in os.environ
# SECURITY WARNING: don't run with debug turned on in production!
if not IS_HEROKU:
    DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'grupotech.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dmgdh1ph6jhif',
        'USER': 'ktwywpzwdeoftz',
        'PASSWORD': '8cc7163b029be691f437ce33411534d562fd19ae9afa0e378e2923282844ff54',
        'HOST': 'ec2-54-91-223-99.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

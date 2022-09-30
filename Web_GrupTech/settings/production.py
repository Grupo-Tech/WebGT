from .base import *
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

IS_HEROKU = "DYNO" in os.environ
# SECURITY WARNING: don't run with debug turned on in production!
if not IS_HEROKU:
    DEBUG = True
else:
    X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = ['127.0.0.1', 'grupotech.herokuapp.com', 'web.grupo-tech.com']

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
        'NAME': 'de35k27l0of6cm',
        'USER': 'hsilqeodwtsfkx',
        'PASSWORD': '928595d7b69e0a418bc401d5d70536d269ac983ebcad0a2433f2553461c0ab49',
        'HOST': 'ec2-44-194-4-127.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

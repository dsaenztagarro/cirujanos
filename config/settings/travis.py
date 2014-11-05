from .testing import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cirujanos_development',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'TEST_NAME': 'cirujanos_test'
    }
}

STATIC_ROOT = '/tmp/static'
MEDIA_ROOT = '/tmp/media'

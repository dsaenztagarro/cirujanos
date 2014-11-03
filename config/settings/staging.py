from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('CIRUJANOS_DATABASE'),
        'USER': os.environ.get('CIRUJANOS_USER'),
        'PASSWORD': os.environ.get('CIRUJANOS_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['cirujanostoracicos.local']

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j1+ihox@!@0ud5+eh77-)7#y9^@n25mhboz@kq8szb+!u@i2*e'

TEMPLATE_DIRS = (
)


COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
)

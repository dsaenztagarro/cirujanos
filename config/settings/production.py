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
        'NAME': os.environ.get('CIRUJANOS_DB'),
        'USER': os.environ.get('CIRUJANOS_USER'),
        'PASSWORD': os.environ.get('CIRUJANOS_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['www.cirujanostoracicos.es', 'cirujanostoracicos.es']

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('CIRUJANOS_SECRET_KEY')

TEMPLATE_DIRS = (
)


COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
)

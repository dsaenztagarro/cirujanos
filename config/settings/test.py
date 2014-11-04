from .base import *

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

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

SOUTH_TESTS_MIGRATE = False

# The default gateway when you setup Virtual box is generally 10.0.2.2 as
# default value.
SELENIUM_COMMAND_EXECUTOR = os.environ.get('CIRUJANOS_COMMAND_EXECUTOR',
                                           'http://10.0.2.2:4444/wd/hub')

LANGUAGE_CODE = 'es-es'

DJANGO_LIVE_TEST_SERVER_ADDRESS = '0.0.0.0:8081'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

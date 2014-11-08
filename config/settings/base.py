import os

# Project folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

DEBUG = bool(os.environ.get('DEBUG', False))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cirujanos_development',
        'USER': 'development',
        'PASSWORD': 'development',
        'HOST': '',
        'PORT': '',
        'TEST_NAME': 'cirujanos_test'
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/var/www/cirujanos/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/var/www/cirujanos/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j1+ihox@!@0ud5+eh77-)7#y9^@n25mhboz@kq8szb+!u@i2*e'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cirujanos.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'cirujanos.wsgi.application'

TEMPLATE_DIRS = (
)

EXTERNAL_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django_extensions',
    # 'django_nose',
    'south',
    'compressor',
    'tinymce',
]

INTERNAL_APPS = [
    'cirujanos',
    'cirujanos.apps.home',
    'cirujanos.apps.about',
    'cirujanos.apps.media',
    'cirujanos.apps.web'
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get('CIRUJANOS_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('CIRUJANOS_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = 'cirujanostoracicos.es <noreply@cirujanostoracicos.es>'

# To print the email into your Command Line Interface once it is sent
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CONTACT_EMAIL_SUBJECT = 'Contactar con cirujanostoracicos.es'

# Asset pipeline
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
)

# HTML Editor configuration
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'theme_advanced_buttons1':
        "save,newdocument,|,bold,italic,underline,strikethrough,|," +
        "justifyleft,justifycenter,justifyright,justifyfull,styleselect," +
        "formatselect,fontselect,fontsizeselect,fullscreen,code",
    'theme_advanced_buttons2':
        "cut,copy,paste,pastetext,|,search,replace,|,bullist,numlist,|," +
        "outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image," +
        "cleanup,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    'theme_advanced_buttons3':
        "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap," +
        "emotions,iespell,media,advhr,|,print,|,ltr,rtl",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_font_sizes': "10px,12px,14px,16px,20px,24px,30px",
    'theme_advanced_resizing': True,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'width': 800,
    'height': 600
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

# Use nose to run all tests
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
# NOSE_ARGS = [
#         '--with-coverage',
#         '--cover-package=cirujanos,cirujanos.apps.home,cirujanos.apps.media,cirujanos.apps.about,cirujanos.apps.web',
#         '--cover-html',
# ]

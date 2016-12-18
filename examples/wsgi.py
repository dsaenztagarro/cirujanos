# vim: set filetype=python:

# See script bin/setup_apache.sh

import os

os.environ['CIRUJANOS_SECRET_KEY'] = 'CIRUJANOS_SECRET_KEY_VAR'
os.environ['CIRUJANOS_DB']         = 'CIRUJANOS_DB_VAR'
os.environ['CIRUJANOS_USER']       = 'CIRUJANOS_USER_VAR'
os.environ['CIRUJANOS_PASSWORD']   = 'CIRUJANOS_PASSWORD_VAR'

os.environ['DJANGO_SETTINGS_MODULE'] = 'DJANGO_SETTINGS_MODULE_VAR'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

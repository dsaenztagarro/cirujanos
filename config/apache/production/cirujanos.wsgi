# vim: set filetype=python:
import os
import sys
import site

project_dir = '/home/cirujanos/apps/cirujanos/releases/current/'
pythonenv_dir = '/var/www/cirujanos/env'

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(pythonenv_dir + '/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append(os.path.expandvars(project_dir))
sys.path.append(os.path.expandvars(project_dir + 'cirujanos'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.production'

# Activate your virtual env
activate_this = pythonenv_dir + "/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

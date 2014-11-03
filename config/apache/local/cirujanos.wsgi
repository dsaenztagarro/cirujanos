# vim: set filetype=python:
import os
import sys
import site

project_dir = '/home/vagrant/Development/projects/cirujanos'
pythonenv_dir = '/var/www/cirujanos/env'

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(pythonenv_dir + '/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append(project_dir)
sys.path.append(project_dir+'cirujanos')

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.local'

# Activate your virtual env
activate_env=os.path.expanduser(pythonenv_dir + "/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

from fabric.api import sudo, env, run, task, local, settings, require
from fabric.contrib import django
from fabric_utils.django import deployment as dep
from fabric_utils.utils import remote_shell_vars, pred
import os
import sys

# 'cirujanos@cirujanostoracicos.es'
env.hosts = [os.environ.get('CIRUJANOS_HOST')]


def get_django_settings():
    # Add project dir to PYTHONPATH so "config.settings" object is found
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    django.settings_module('config.settings.%s' % env.environment)
    from django.conf import settings as django_settings
    return django_settings


@task
def host():
    """
    Set localhost environment context. An exception is thrown if there is a
    missing fabricrc attribute
    Example of use: fab host deploy -c config/apache/local/fabricrc
    """
    check_host_env()
    env.environment = 'local'
    env.run = local
    env.hosts = ['localhost']
    env.shell_vars = {
        "home": env.home_path
    }


def check_host_env():
    """
    Checks that all environment attributes are defined in fabricrc
    """
    attributes = ["project_name", "release_path", "www_path", "home_path"]
    for attr in attributes:
        if not hasattr(env, attr):
            pred(("ERROR: Undefined '%s' attribute.\n"
                  "More info in README.") % attr)
            exit()


@task
def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['192.168.10.10']

    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]

    env.project_name = 'cirujanos'
    env.environment = 'development'
    env.path = os.path.expandvars('/home/vagrant/apps/%s' % env.project_name)
    env.www_path = '/var/www/cirujanos'
    env.virtualhost_path = '/'


@task
def remote():
    "Set production environment context"
    env.project_name = 'cirujanos'
    env.environment = 'production'
    env.run = run
    # env.hosts = ['www.cirujanostoracicos.es']
    # env.release_path generated by symlink_current_release
    env.www_path = '/var/www/cirujanos'
    env.shell_vars = remote_shell_vars()
    # generate release path
    env.path = os.path.expandvars('/home/cirujanos/apps/%s' % env.project_name)
    # ?
    env.virtualhost_path = '/'


@task
def deploy():
    if env.environment is not "local":
        require('hosts', provided_by=[local])
        require('path')
        dep.generate_release_path()
        dep.upload_source()
        dep.symlink_current_release()

    dep.install_requirements()
    dep.migrate()
    dep.install_static()
    dep.compress_static()
    dep.compile_messages(['cirujanos/apps/media', 'cirujanos/apps/about'])
    dep.www_folder_permissions()
    dep.install_site()
    dep.restart_webserver()


@task
def setup():
    """
    (Deprecated) Use Chef Server whenever possible
    Setup a fresh virtualenv as well as a few useful directories, then run
    a full deployment
    """
    require('hosts', provided_by=[local])
    require('path')

    sudo(('aptitude install -y python-setuptools; '
          'easy_install pip; '
          'pip install virtualenv; '
          'aptitude install -y apache2; '
          'aptitude install -y libapache2-mod-wsgi; '
          'apt-get install -y mysql-server; '
          'apt-get install python-setuptools python-dev build-essential; '
          'apt-get install libmysqlclient-dev; '
          'apt-get install python-mysqldb; '
          'apt-get install gettext; '
          # 'apt-get install nodejs npm && sudo npm install coffee-script; '
          'apt-get install coffeescript; '
          ))

    # we want rid of the defult apache config
    sudo(('cd /etc/apache2/sites-available; '
          'a2dissite default; '
          'mkdir -p ' + env.www_path + '/static; '
          'mkdir -p ' + env.www_path + '/media; '
          'cd ' + env.www_path + '; '
          'virtualenv env; '))

    with settings(warn_only=True):
        run(('mkdir -p ' + env.path + '; '
             'cd ' + env.path + '; '
             'mkdir -p releases; '
             'mkdir -p shared; '
             'mkdir -p packages; '))

    # also installed manually:
    # - git
    # - node version with bower compatible module
    # - bower
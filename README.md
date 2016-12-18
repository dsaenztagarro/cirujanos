# Django cirujanos #

[![Build Status](https://travis-ci.org/dsaenztagarro/cirujanos.svg?branch=master)](https://travis-ci.org/dsaenztagarro/cirujanos)
[![Coverage Status](https://coveralls.io/repos/dsaenztagarro/cirujanos/badge.png?branch=master)](https://coveralls.io/r/dsaenztagarro/cirujanos?branch=master)

## Deploy with Apache mod_wsgi

Check `Vagrantfile` for packages to be installed in Ubuntu machine.

As sudo:

```
mkdir -p /var/www/cirujanos
chown -R cirujanos:www-data /var/www/cirujanos
```

Before setup:

```
cd /var/www/cirujanos
git clone -b <branch-name> <git-repository> .
virtualenv -p /usr/bin/python3.5 venv
source venv/bin/activate
```

Copy the script bin/setup_apache.sh and fill the gaps.

Setup:

```
./bin/setup_apache.sh
cd /var/www/cirujanos
make setup
cp -f examples/apache2/sites-available/cirujanos.conf /etc/apache2/sites-available/
make setup
a2ensite cirujanos.conf
```

### References

- [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/es/1.10/howto/deployment/wsgi/modwsgi/)
- [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/index.html)

## Setup development environment (under review)

Checking Django version installed

```
python -m django --version
```

Just execute these commands in your virtualenv(wrapper):

```shell
pip install -r requirements-devel.txt
# To replicate production environment
manage.py reset_db
fab restore_db
# Always
manage.py syncdb
manage.py migrate
```

## Running tests locally ##

```
coverage run --source='.' manage.py test cirujanos --liverserver=0.0.0.0:8081 --settings=config.settings.testing
# Optionally:
coverage html --include="cirujanos/*"
coverage report
```

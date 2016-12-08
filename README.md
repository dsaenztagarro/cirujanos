# Django cirujanos #

[![Build Status](https://travis-ci.org/dsaenztagarro/cirujanos.svg?branch=master)](https://travis-ci.org/dsaenztagarro/cirujanos)
[![Coverage Status](https://coveralls.io/repos/dsaenztagarro/cirujanos/badge.png?branch=master)](https://coveralls.io/r/dsaenztagarro/cirujanos?branch=master)

## Setup development environment ##

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

## Pending tasks

- [ ] Lettuce
- [ ] Documentation
- [ ] 100% coverage

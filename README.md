[![Build Status](https://travis-ci.org/dsaenztagarro/django-cirujanos.svg?branch=master)](https://travis-ci.org/dsaenztagarro/django-cirujanos)
[![Coverage Status](https://coveralls.io/repos/dsaenztagarro/django-cirujanos/badge.png?branch=master)](https://coveralls.io/r/dsaenztagarro/django-cirujanos?branch=master)

# Tests

```
PYTHONPATH=`pwd` py.test cirujanos

coverage run --source='.' manage.py test cirujanos --liverserver=0.0.0.0:8081
coverage html --include="cirujanos/*"
coverage report
```

When you're using a minimal Ubuntu install if you find the
'add-apt-repository' command is missing (it's useful for adding PPAs and other
repositories), then simply run:
`sudo apt-get install python-software-properties`

Install Firefox:

```
sudo add-apt-repository ppa:ubuntu-mozilla-security/ppa
sudo apt-get update
sudo apt-get install firefox
```


## Translations

Created locale dir: mkdir locale  
Updated main.settings.py: LANGUAGE_CODE = "es-es"  
If you execute the next command then a template is generated: 

```
django-admin.py makemessages -l es_ES  
PROJECT/APP/locale/es_ES/LC_MESSAGES/django.po
```

If you find this message:
> CommandError: Error running xgettext. Note that Django internationalization
  requires GNU gettext 0.15 or newer.
  
Then execute:

```
brew install gettext
brew link gettext --force
```

If you execute the next command then the translation message file is compiled,
generating a new file

```
django-admin.py compilemessages
PROJECT/APP/locale/es_ES/LC_MESSAGES/django.mo
```

## Upgrades

```
pip install django --upgrade
yolk -l
```

# Tests
- - -

```
./manage.py test cirujanos_web.tests.views
```

Added property to DATABASE configuration in main/settings.py:

```
'TEST_NAME': 'test_cirujanos'
```

If not found this property the name of the test database will be

```
"test_" + database_name
```

Executed command: `python manage.py test cirujanos_web --verbosity=2`  
Test database will be recreated and **initial_data** scripts will be loaded  
Note: To create initial_data scripts from development database:

```
python manage.py dumpdata cirujanos_web --format=yaml > ...
```

Tip: Getting json fixtures from MySQL database:

```
mysql2json --user=devuser --password=devuser --execute="select * from cirujanos_web_doctor" --database=dev_cirujanos
mysql2json -u devuser -p devuser -e "select * from cirujanos_web_doctor" -d dev_cirujanos > app/fixtures/doctor_testdata.json
```

You will need to modify the testdata file adding for each model:

```
{"pk": 1, "model": "cirujanos_web.doctor", "fields": { ... content ... }}
```

Warning: if there is a error404 page, then the next assertion will be always true:

```
self.assertEqual(resp.status_code, 200)
```

# Deployment
- - -
## Apache (mod WSGI)

### Loading initial data configuration

Delete all migrations of an app from database:
`./manage.py migrate about zero --fake`

Loading fixtures:
`./manage.py loaddata about about/fixture/doctor_content_type_fixture.json`


## Todo

- [ ] Lettuce
- [ ] Move to fabricrc package env path

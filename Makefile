.PHONY: setup

DJANGO_ENV = local

PYTHON_INTERPRETER = /usr/local/bin/python3.5

UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)

	CFLAGS = -I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers \
					 -I/usr/local/opt/zlib/include \
					 -I/usr/local/opt/openssl/include \
					 -I/usr/local/Cellar/libyaml/0.1.7/include

	LDFLAGS = -L/usr/local/opt/openssl/lib \
						-L/usr/local/Cellar/libyaml/0.1.7/lib

	CFLAGS_FABRIC = -I/usr/local/Cellar/gmp/6.1.0/include
	LDFLAGS_FABRIC = -L/usr/local/Cellar/gmp/6.1.0/lib

endif

PIP = LDFLAGS="$(LDFLAGS)" CFLAGS="$(CFLAGS)" pip install --ignore-installed -r

setup:
	$(PIP) requirements.txt
	bower install --production
	python manage.py collectstatic --no-input
	python manage.py compress
	django-admin compilemessages

setup-dev:
	$(PIP) requirements-dev.txt
	bower install

runserver:
	python manage.py runserver --settings=config.settings.$(DJANGO_ENV)

syncr:
	pip freeze > requirements.txt

install_fabric:
	CFLAGS="$(CFLAGS_FABRIC)" LDFLAGS="$(LDFLAGS_FABRIC)" pip install -r requirements_fabric.txt --ignore-installed


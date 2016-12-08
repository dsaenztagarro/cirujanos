.PHONY: setup

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

setup:
	virtualenv -p $(PYTHON_INTERPRETER) venv

runserver:
	python manage.py runserver --settings=config.settings.local

syncr:
	pip freeze > requirements.txt

install:
	LDFLAGS="$(LDFLAGS)" CFLAGS="$(CFLAGS)" pip install -r requirements.txt --ignore-installed

install_fabric:
	CFLAGS="$(CFLAGS_FABRIC)" LDFLAGS="$(LDFLAGS_FABRIC)" pip install -r requirements_fabric.txt --ignore-installed

upgrade:
	CFLAGS="$(CFLAGS)" pip install -r requirements.txt --upgrade
	pip freeze > requirements.txt


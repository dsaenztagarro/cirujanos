.PHONY: setup

WORKING_DIR = $(HOME)/Code/Python/cirujanos

TK_INCLUDE   = -I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers
ZLIB_INCLUDE = -I/usr/local/opt/zlib/include
SSL_INCLUDE  = -I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib

CFLAGS = $(TK_INCLUDE) $(ZLIB_INCLUDE) $(SSL_INCLUDE)

VIRTUALENV = $(HOME)/Code/Python/Virtualenvs/cirujanos/bin/activate

install:
	CFLAGS="$(CFLAGS)" pip install -r requirements.txt --ignore-installed

upgrade:
	CFLAGS="$(CFLAGS)" pip install -r requirements.txt --upgrade
	pip freeze > requirements.txt


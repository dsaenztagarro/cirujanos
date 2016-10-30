.PHONY: setup

WORKING_DIR = $(HOME)/Code/Python/cirujanos

TK_INCLUDE   = -I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers
ZLIB_INCLUDE = -I/usr/local/opt/zlib/include
SSL_INCLUDE  = -I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib

CFLAGS = $(TK_INCLUDE) $(ZLIB_INCLUDE) $(SSL_INCLUDE)

install:
	CFLAGS="$(CFLAGS)" pip install -r requirements-devel.txt --ignore-installed


from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = '%s/static_media/static' % BASE_DIR
MEDIA_ROOT = '%s/static_media/media' % BASE_DIR

COMPRESS_ENABLED = False
COMPRESS_ROOT = BASE_DIR
COMPRESS_OUTPUT_DIR = STATIC_ROOT

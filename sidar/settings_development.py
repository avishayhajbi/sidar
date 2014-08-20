# -*- coding: utf-8 -*-
from sidar.settings_common import *
import sys

MEDIA_ROOT = 'media/'
DEBUG = TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['localhost', ]
PORTFOLIO_CSV_ROOT = u'/Volumes/d$/המכון לעיצוב/מחלקות עיצוב'   # \\design26\d$\המכון לעיצוב\מחלקות עיצוב
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Don't set up legacy database during testing
# if 'test' not in sys.argv:
#    for name in LEGACY_DB_NAMES:
#        DATABASES[name] = {
#            'ENGINE': 'django.db.backends.mysql',
#            'NAME': name,
#            'USER': 'root',
#            'PASSWORD': 'sidar',
#            'HOST': '',
#            'PORT': '',
#        }

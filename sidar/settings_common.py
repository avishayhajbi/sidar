# Django settings for sidar project.
# -*- coding: utf-8 -*-

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
DEBUG = False

AUTH_PROFILE_MODULE = 'backoffice.UserProfile'

DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_FILESYSTEM_DIRECTORY = '~/Backup'
SOUTH_TESTS_MIGRATE = True
# PORTFOLIO_CSV_ROOT = "/Users/danielbraun/Development/design26d"
# PORTFOLIO_CSV_ROOT = u'/Volumes/m$/D/המכון לעיצוב/מחלקות עיצוב'
# DEBUG = True
TEMPLATE_DEBUG = DEBUG

LOGIN_URL = '/'
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

LEGACY_DB_NAMES = ['php_gd', 'php_id']


# for name in LEGACY_DB_NAMES:
#     DATABASES[name] = {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': name,
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Jerusalem'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'he'

# LANGUAGES = (
#     ('he', u'Hebrew'),
#     ('en', u'English'),
#     # ('ar', u'Arabic'), Disable this comment to enable Arabic translation
# )
gettext = lambda s: s
LANGUAGES = (
    ('he', gettext('Hebrew')),
    ('en', gettext('English')),
)

MODELTRANSLATION_TRANSLATION_REGISTRY = 'backoffice.translation'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = 'collected_static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '**&amp;6s=rn2(0@a4@c3m4#^15jom%@x5p21&amp;$#nc^udo+dzd-68#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'backoffice.context_processors.default',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'sidar.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sidar.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'moderation',
    'backoffice',
    'south',
    'imagekit',
    'modeltranslation',
    'dbbackup',
    'gunicorn',
    'bibliography',
    'collection',
    'django.contrib.flatpages',
    'feedback',
    'taggit',
    'timeline',
    'tinymce',
    'flatpages_tinymce',
    'django_countries',
    'storages',
    'form_utils',
    'django_filters',
    'jquery',
    'url_tools',
    'registration',
    'links',
    'articles',
    'videos',
    'events',
    # 'debug_toolbar',
    'importer',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

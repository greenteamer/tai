# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os

from django.utils.translation import ugettext_lazy as _
from os.path import abspath, dirname, basename, join, split
from easy_thumbnails.conf import Settings as thumbnail_settings

CURRPATH = os.path.abspath('.')

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

LOCKDOWN_FORM = 'lockdown.forms.AuthForm'
LOCKDOWN_AUTHFORM_SUPERUSERS_ONLY = True
LOCKDOWN_PASSWORDS = ('letmein', 'beta')

DEBUG = True

#TEMPLATE_DEBUG = DEBUG

BREADCRUMBS_AUTO_HOME = True

DEFAULT_CHARSET = 'utf-8'

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS


ADMINS = (
	# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'ru'

ugettext = lambda s: s

LANGUAGES = (
	('en', ugettext('English')),
	('ru', ugettext('Russian')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# MEDIA_ROOT = 'C:/webmagazinedjango/webshop/static/media/'
# MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media').replace('\\', '/')
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join(PROJECT_PATH, 'static').replace('\\', '/'),
	os.path.join(PROJECT_PATH, 'static/media').replace('\\', '/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'rs!w229&m79-)f3ohat)gd=u7q)^3#3(*1)k4-)*qwc^4zgom9'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    # 'lockdown.middleware.LockdownMiddleware',
    #'webshop.SSLMiddleware.SSLRedirect',
)

ROOT_URLCONF = 'webshop.urls'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join(PROJECT_PATH, 'templates').replace('\\', '/'),
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
	'webshop.utils.context_processors.webshop',
)
if DEBUG:
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

DAJAXICE_MEDIA_PREFIX="dajaxice"

DAJAX_FUNCTIONS=(
    'webshop.ajaxapp.onload_cart',
    'webshop.ajaxapp.calc_delivery',
    'webshop.ajaxapp.change_atrs',
)

SOUTH_MIGRATION_MODULES = {
    'captcha': 'captcha.south_migrations',
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}


INSTALLED_APPS = (

    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.flatpages',
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
    'south',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
	# Custom modules
    'webshop.catalog',
    'webshop.cart',
    'webshop.accounts',
    'webshop.checkout',
    'webshop.news',
    'webshop.search',
    'webshop.ajaxapp',
    'webshop.slider',
    'webshop.pages',
    'mptt',
    'bootstrap3',
    'sorl.thumbnail',
    'dajaxice',
    'dajax',
    'captcha',
    'robokassa',
    'breadcrumbs',
    'easy_thumbnails',
    'image_cropping',
    'ckeditor',
    'mptt_tree_editor',
    # 'lockdown',
)

THUMBNAIL_DEBUG = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
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


# Custom settings
ENABLE_SSL = False
SITE_NAME = _(u'Product magazine')
META_KEYWORDS = _(u'products, online, shop, buy')
META_DESCRIPTION = _(u'Product magazine is an online supplier of products')
LOGIN_REDIRECT_URL = '/accounts/my_account/'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 90 # 90 дней на хранение cookies
PRODUCTS_PER_PAGE = 300
AUTH_PROFILE_MODULE = 'accounts.UserProfile'

ROBOKASSA_LOGIN = 'polythai'
ROBOKASSA_PASSWORD1 = 'polythai2014'
ROBOKASSA_PASSWORD2 = 'polythai2014secondPass'
ROBOKASSA_TEST_MODE = False

try:
    from settings_local import *
except ImportError:
    pass

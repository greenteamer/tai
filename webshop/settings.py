# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
from easy_thumbnails.conf import Settings as thumbnail_settings
from django.utils.translation import ugettext_lazy as _

CURRPATH = os.path.abspath('.')

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
ALLOWED_HOSTS = ['*']
# TEMPLATE_DEBUG = DEBUG

BREADCRUMBS_AUTO_HOME = True

DEFAULT_CHARSET = 'utf-8'

THUMBNAIL_PROCESSORS = (
                           'image_cropping.thumbnail_processors.crop_corners',
                       ) + thumbnail_settings.THUMBNAIL_PROCESSORS

ADMINS = (
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

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'en-us'
ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext('English')),
    ('ru', ugettext('Russian')),
)

SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

SECRET_KEY = 'rs!w229&m79-)f3ohat)gd=u7q)^3#3(*1)k4-)*qwc^4zgom9'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
)
ROOT_URLCONF = 'webshop.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'webshop/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DAJAXICE_MEDIA_PREFIX="dajaxice"

DAJAX_FUNCTIONS=(
    'webshop.ajaxapp.onload_cart',
    'webshop.ajaxapp.calc_delivery',
    'webshop.ajaxapp.change_atrs',
    'webshop.ajaxapp.addToCart',
)

SOUTH_MIGRATION_MODULES = {
    'captcha': 'captcha.south_migrations',
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.admin',

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
    'mptt_tree_editor',
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
    'rest_framework',
)

THUMBNAIL_DEBUG = True

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
SESSION_COOKIE_AGE = 60 * 60 * 24 * 90  # 90 дней на хранение cookies
PRODUCTS_PER_PAGE = 300
AUTH_PROFILE_MODULE = 'accounts.UserProfile'

try:
    from settings_local import *
except ImportError:
    pass

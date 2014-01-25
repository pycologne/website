# -*- coding: utf-8 -*-
"""Basic configuration for this Django project."""

import os

from django.utils.translation import ugettext_lazy as _

from pycologne.settings import *

PROJECT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__),
                               '..', '..'))

gettext = lambda s: s

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

LANGUAGES = [
    ('de', gettext(u'German')),
]

TIME_ZONE = 'Europe/Berlin'

LANGUAGE_CODE = 'de-de'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'staticfiles', 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles', 'static')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'pycologne.urls'

INSTALLED_APPS = (
    # custom Apps for PyCologne Website
    'pycologne.events',
    'pycologne.website',
    # Custom administration
    'admin_shortcuts',
    'djangocms_admin_style',
    # Default Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django-reversion',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # For Django-CMS
    'djangocms_text_ckeditor', # note this needs to be above the 'cms' entry
    'cms',
    'mptt',
    'menus',
    'sekizai',
    #'djangocms_style',
    #'djangocms_column',
    'cms.plugins.file',
    'cms.plugins.googlemap',
    #'cms.plugins.inherit',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.teaser',
    'cms.plugins.video',
    #'reversion',
    # Other
    'easy_thumbnails',
    'south',
    'compressor',
    'django_rj_utils',
    'bootstrap_toolkit',
    'bootstrap_pagination',
    # future:
    # 'piwik',
    # 'filer',
    # 'taggit',
    # 'cmsplugin_filer_image',
    'userprofiles',
    'userprofiles.contrib.accountverification',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'pycologne', 'website', 'templates',
                 'website'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
)

WSGI_APPLICATION = 'pycologne.wsgi.application'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

LOCALE_PATHS = [
    os.path.join(PROJECT_DIR, 'pycologne', 'locale'),
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# DjangoCMS
# Cannot be empty!
CMS_TEMPLATES = (
    ## Customize this
    ('default.html', 'Default'),
    ('home.html', 'Home'),
    # ('index.html', 'Home (index)'),
    ('demo.html', 'Demo (static page)')
    # TODO - add custom templates!
)

###CMS_PLACEHOLDER_CONF = {
    ###'content': {
        ###'plugins': ['TextPlugin', 'PicturePlugin'],
        ###'text_only_plugins': ['LinkPlugin'],
        ###'extra_context': {"width": 640},
        ###'name': gettext("Content"),
    ###}
###}


# Important! Less must be installed: http://lesscss.org/#-server-side-usage
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

# Admin Shortcuts
ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
            },
            {
                'url_name': 'admin:cms_page_changelist',
                'title': _(u'Pages'),
            },
        ]
    },
]

USERPROFILES_CHECK_UNIQUE_EMAIL = True
USERPROFILES_USE_ACCOUNT_VERIFICATION = True

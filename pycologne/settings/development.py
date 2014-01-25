# -*- coding: utf-8 -*-
"""Config for development."""

from pycologne.settings import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

COMPRESS_PRECOMPILERS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'pycologne', 'dev.db'),
        'ATOMIC_REQUESTS': True
    }
}

MIDDLEWARE_CLASSES += (
    #'devserver.middleware.DevServerMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    #'devserver',
    'debug_toolbar',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

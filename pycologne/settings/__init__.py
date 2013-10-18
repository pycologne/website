# -*- coding: utf-8 -*-
"""Loads all available config files."""

import os


ENV = os.environ.get('ENV', 'development')

from base import *

if ENV == 'production':
    from production import *
elif ENV == 'development':
    from development import *
elif ENV == 'staging':
    from staging import *

try:
    from local import *
except ImportError:
    pass

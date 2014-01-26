# -*- coding: utf-8 -*-
"""Fab commands that are running on remotes."""

from __future__ import with_statement

import os
from os.path import expanduser, isfile, join

from fabric.api import *
from fabric.context_managers import shell_env

USER = 'pycologne'
HOME = '/home/www/pycologne.de'
ENV = os.getenv('ENV', 'staging')
SITE_NAME = ENV
PROJECT_NAME = 'pycologne'
PROJECT_DIR = join(HOME, 'sites', SITE_NAME)
VIRTUAL_ENV_NAME = '%s-%s' % (PROJECT_NAME, SITE_NAME)

env.hosts = ['%s@pycologne.de' % USER]

if env.ssh_config_path and isfile(expanduser(env.ssh_config_path)):
    env.use_ssh_config = True


def supervisord(task='start'):
    """Controls the supervisord."""
    if task == 'start':
        with prefix('workon %s' % VIRTUAL_ENV_NAME):
            run('supervisord -c "%s/etc/supervisord.conf"' % HOME)
    elif task == 'stop':
        supervisorctl('shutdown')
    elif task == 'restart':
        supervisord('stop')
        supervisord('start')


def supervisorctl(task):
    """Controls the supervisor."""
    with prefix('workon %s' % VIRTUAL_ENV_NAME):
        run('supervisorctl -c "%s/etc/supervisor.conf" %s %s' %
            (HOME, task, SITE_NAME))


def memcached(task='start'):
    """Controls the memcached."""
    if task == 'start':
        run('memcached -d -m 256 -P %s/var/run/memcached.pid' % HOME)
    elif task == 'stop':
        run('kill $(cat %s/var/run/memcached.pid)' % HOME)
    elif task == 'restart':
        memcached('stop')
        memcached('start')


def nginx(task='reload'):
    """Controls the nginx webserver."""
    run('nginx -s %s' % task)


def update_source():
    """Updates the project."""
    with cd(PROJECT_DIR), prefix('workon %s' % VIRTUAL_ENV_NAME):
        run('git pull')
        run('pip install --no-deps -Ur requirements/stable.req.txt')
        with shell_env(ENV=ENV):
            run('./manage.py syncdb --migrate')
            run('./manage.py collectstatic --noinput')


def clear_remote_static_cache():
    """Clears the django compressor cache on the remote server."""
    with cd(PROJECT_DIR), prefix('workon %s' % VIRTUAL_ENV_NAME), shell_env(ENV=ENV):
        run('fab clear_static_cache')


def deploy():
    """Deploys."""
    supervisorctl('stop')
    update_source()
    clear_remote_static_cache()
    supervisorctl('start')
    memcached('start')

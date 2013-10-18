# -*- coding: utf-8 -*-
"""Fab commands that are running on remotes."""

from __future__ import with_statement
from fabric.api import *
from fabric.context_managers import shell_env

env.hosts = []

PROJECT_NAME = 'pycologne'
PROJECT_DIR = 'UPDATE/%s' % PROJECT_NAME
VIRTUAL_ENV_NAME = 'UPDATE'


def supervisord(task='start'):
    """Controls the supervisord."""
    if task == 'start':
        with prefix('workon %s' % VIRTUAL_ENV_NAME):
            run('supervisord -j $HOME/supervisord.pid')
    elif task == 'stop':
        run('kill $(cat $HOME/supervisord.pid)')
    elif task == 'restart':
        supervisord('stop')
        supervisord('start')


def supervisorctl(task):
    """Controls the supervisor."""
    run('supervisorctl %s %s' % (task, PROJECT_NAME))


def memcached(task='start'):
    """Controls the memcached."""
    if task == 'start':
        run('memcached -d -m 256 -P $HOME/memcached.pid')
    elif task == 'stop':
        run('kill $(cat $HOME/memcached.pid)')
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
        with shell_env(ENV='production'):
            run('./manage.py syncdb --all --migrate')
            run('./manage.py collectstatic --noinput')


def clear_remote_static_cache():
    """Clears the django compressor cache on the remote server."""
    with cd(PROJECT_DIR), prefix('workon %s' % VIRTUAL_ENV_NAME):
        with shell_env(ENV='production'):
            run('fab clear_static_cache')


def deploy():
    """Deploys."""
    supervisorctl('stop')
    update_source()
    clear_remote_static_cache()
    supervisorctl('start')
    memcached('start')
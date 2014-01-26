PyCologne Website
=================

This is the code for the website of the Python UserGroup Cologne pyCologne_.

.. _pycologne: http://www.pycologne.de


Development
-----------


Pre-Requirements
++++++++++++++++

* Python 2
* virtualenv
* PostgreSQL
* sqlite3

(including header files, i.e. on debian-like systems install the
'postgresql-dev' package)

.. _less: http://www.lesscss.org/


Installation
++++++++++++

1. Either:

    - Clone this repository directly (website team members)::

        $ git clone https://github.com/pycologne/website.git

    - Or fork this repository and clone your fork (others).

3. Make a virtual environment using mkvirtualenv or mkproject, e.g.::

    $ mkvirtualenv [--no-site-packages] pycologne-website

4. Install packages necessary for bootstrapping::

    $ pip install django fabric

5. Change into the checkout directory and run::

    $ python -c "import uuid; print('SECRET_KEY = \"%s\"' % uuid.uuid1())" > \
        pycologne/settings/local.py
    $ fab install_dev_requirements
    $ python manage.py syncdb --all
    $ python manage.py migrate --fake
    $ python manage.py compilemessages

6. Run the development server::

    $ fab devserver

7. Send pull requests.

That's it! Happy developing :)


Staging server setup
--------------------

.. note::
    Commands noted below prefixed by a dollar-sign (``$``) prompt are shell
    commands and should be entered without that prompt.

#. Install prerequisites via your distribution's package manager::

        $ sudo apt-get install build-essential curl git-core \
            python python-dev python-virtualenv python-pip postgresql nginx

   .. _note::
        Make sure that the Python packages you install are for Python 2.7. On
        newer distribution you might have to change the ``python`` part in the
        package names to ``python2``.

#. Set up a dedicated user for the application on the server::

        $ sudo mkdir /home/www
        $ sudo adduser --home /home/www/pycologne.de pycologne

#. Install virtualenvwrapper and set it up for the application user::

        $ sudo pip install virtualenvwrapper

#. Create a PostgresSQL database (on debian do this as the user ``postgres``)::

        $ su - postgres
        (postgres)$ createuser -P -D -R -S pycologne-staging
        (postgres)$ createdb -O pycologne-staging pycologne-staging

#. Edit ``/etc/postgresql/9.1/main/pg_hba.conf`` and add this line::

        local pycologne-staging pycologne-staging md5

   **after** the one that reads::

        local   all     postgres    ident

   (for a local trusted development machine, you might want to use instead)::

        host    all         all         127.0.0.1/32                trust

   and reload the PostgreSQL configuration::

        sudo service postgresql reload

Now, log in as the new user ``pycologne``. The following steps should all be
carried out as this user, unless stated otherwise.

#. Add the following to the end of ``~ /.profile`` (or ``~/.bash_profile``, if
   you have it)::

        if [ -d "$HOME/local" ] ; then
            PATH="$HOME/local/bin:$PATH"
        fi

        export WORKON_HOME=$HOME/lib/venvs
        export PIP_VIRTUALENV_BASE=$WORKON_HOME
        export PIP_RESPECT_VIRTUALENV=true
        export PIP_DOWNLOAD_CACHE="$HOME/.pip_download_cache"

        source /usr/local/bin/virtualenvwrapper.sh

#. And create a few directories::

        $ mkdir -p ~/bin ~/etc ~/lib/venvs ~/local ~/sites \
            ~/var/{log,run,tmp} ~/.pip_download_cache

#. Log out and log in again as user ``pycologne`` for the environment changes
   to take effect. On logging in you will see a bunch of messages by
   virtualenvwrappper while it creates some scripts under ``$WORKON_HOME``.

#. Install Node.js_ (from source)::

        $ cd ~/var/tmp
        $ curl http://nodejs.org/dist/node-latest.tar.gz | tar -xz
        $ cd node-v0.10.*
        $ ./configure --prefix=~/.local
        $ make install

   You can go and have a LARGE coffee while Node.js compiles.

#. Install LESS_::

        $ npm install less

#. Create a virtualenv ``pycologne-staging``::

        mkvirtualenv -p /usr/bin/python2 pycologne-staging

   The following commmands assume that you have activated the virtual
   environment ``pycologne-staging`` in your current shell.

#. Check out the application code::

        $ mkdir -p ~/sites
        $ cd ~/sites
        $ git clone https://github.com/pycologne/website.git staging

#. Create the file ``~/sites/staging/pycologne/settings/local.py`` with the
   following content and change the password for the Postgres database user
   ``pycologne-staging`` in the ``DATABASES`` configuration directory to the
   one you chose above::

        import os

        if os.environ.get('ENV') == 'staging':
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': 'pycologne-staging',
                    'USER': 'pycologne-staging',
                    'PASSWORD': 'thepassword'
                }
            }

        ALLOWED_HOSTS = ["staging.pycologne.de"]

   Make sure this file is not world-readable::

        $ chmod 640 ~/sites/staging/pycologne/settings/local.py

#. Install the application and initialize the database, message catalogs and
   static files::

        $ cd ~/sites/staging
        $ pip install django fabric
        $ python -c "import uuid;print('SECRET_KEY = \"%s\"'%uuid.uuid1())" \
            >> pycologne/settings/local.py
        $ fab install_stable_requirements
        $ ENV=staging python manage.py syncdb --all
        $ ENV=staging python manage.py migrate --fake
        $ ENV=staging python manage.py compilemessages
        $ ENV=staging python manage.py collectstatic --noinput

   Choose a user name and a secure password for the django CMS adminstration
   user when prompted. You will need those later to log into the web
   administration frontend.

#. (As root) Install the Nginx configuration::

        $ sudo install -m 644 config/ngingx.conf \
            /etc/nginx-sites-available/staging.pycologne.de
        $ sudo ln -s ../sites-available/staging.pycologne.de \
            /etc/nginx/sites-enabled

   Make the log directory writable for the user Nginx runs under (normally
   ``www-data``)::

        $ sudo chgrp www-data ~/var/log
        $ sudo chmod g+w ~/var/log

   Then reload the Nginx configuration::

        $ sudo service nginx reload

#. Install the supervisor daemon configuration::

        $ install -m 640 config/supervisor{,d}.conf ~/etc
        $ mkdir ~/etc/supervisor.conf.d
        $ install -m 640 config/supervisord-pycologne.conf \
            ~/etc/supervisord.conf.d/pycologne.conf

#. Finally, you should now be able to start the application server via
   supervisor::

        $ supervisord -c ~/etc/supervisord.conf

   You can check the status of the application server with supervisorctl::

        $ supervisorctl -c ~/etc/supervisor.conf status

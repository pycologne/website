PyCologne Website
=================


This is the website of the Python UserGroup Cologne.

http://www.pycologne.de


Development
-----------


Pre-Requirements
++++++++++++++++

* Python 2
* virtualenv
* postgresql
* sqlite3

  (including header files, i.e. on debian-like systems install the
  'postgresql-dev' package)


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
    $ fab install_dev_requirements syncdb mo

6. Run the development server::

    $ fab devserver

7. Send pull requests.

That's it! Happy developing :)


Server setup
------------

#. Set up a dedicated user for the application on the server.

#. Install virtualenvwrapper and set it up for the application user.

#. Create a virtualevnv ``pycologne-staging``for the staging server or
   ``pycologne-prod`` for the production server.

#. ::

        $ mkdir -p ~/sites/{staging,prod}
        $ cd ~/sites
        $ git clone https://github.com/pycologne/website.git staging
        $ cd staging

#. Create a PostgresSQL database (on debian do this as the user ``postgres``)::

        $ createuser -P -D -R -S pycologne-staging
        $ createdb -O pycologne-staging pycologne-staging

#. Edit ``/etc/postgresql/9.1/main/pg_hba.conf`` and add this line::

        local pycologne-staging pycologne-staging md5

   **after** the one that reads:

        local   all         postgres                          ident

   and reload the PostgreSQL configuration::

        service postgresql reload

   (for a local trusted development machine, you might want to use instead:)

        host    all         all         127.0.0.1/32                trust
        

#. Follow steps 4. and 5. under Installation

#. TBC...

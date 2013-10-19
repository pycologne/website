pyCologne website
=================


This is the website of the Python UserGroup Cologne.
http://www.pycologne.de

Development
-----------

Installation
++++++++++++

1. Either:

    - Clone this repository directly (website team members)::

        $ git clone https://github.com/pycologne/website.git

    - Or fork this repository and clone your fork (others).

3. Make a virtual environment, e.g.::

    $ mkvirtualenv [--no-site-packages] pycologne-website

4. Install packages necessary for bootstrapping::

    $ pip install django fabric

5. Change into the checkout directory and run::

    $ python -c "import uuid; print('SECRET_KEY = \"%s\"' % uuid.uuid1())" > \
        pycologne/settings/local.py
    $ fab install_dev_requirements syncdb mo

6. Run the development server::

	$ ./manage.py runserver

7. Send pull requests.


That's it! Happy developing :)

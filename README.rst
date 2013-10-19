pyCologne website
=================


This is the website of the Python UserGroup Cologne.
http://www.pycologne.de

Development
-----------

Installation
++++++++++++

1. Either:

    - Fork this repository and clone your fork

3. Make a virtual environment, e.g.::

    mkvirtualenv [--no-site-packages] pycologne-website

4. Install packages necessary for bootstrapping::

    pip install django fabric

4. Change into the checkout directory and run::

    $ fab install_dev_requirements syncdb mo

5. Run the development server::

	$ ./manage.py runserver

6. Send pull requests.


That's it! Happy developing :)

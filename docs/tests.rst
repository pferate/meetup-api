Testing
=======

Before contributing to Meetup API, make sure your patch passes the test suite
and your code style passes the code linting suite.

Meetup API uses `Tox`_ to execute testing and linting procedures. Tox is the
only dependency you need to run linting or the test suite, the remainder of the
requirements will be installed by Tox into environment specific virtualenv
paths. Before testing, make sure you have Tox installed::

    pip install tox

To run the full test and lint suite against your changes, simply run Tox. Tox
should return without any errors. You can run Tox against all of the
environments by running::

    tox

To target a specific environment::

    tox -e py27

The ``tox`` configuration has the following environments configured. You can
target a single environment to limit the test suite:

========  ======================================================
Env Name  Description
========  ======================================================
py26      Run the test suite using Python 2.6
py27      Run the test suite using Python 2.7
py34      Run the test suite using Python 3.4
py35      Run the test suite using Python 3.5
coverage  Run the test suite and check code coverage
flake8    Run code linting using `flake8`_.  This currently runs
          `pyflakes`_, `pep8`_, and other linting tools.
docs      Test documentation compilation with Sphinx.
========  ======================================================

.. _`Tox`: http://tox.readthedocs.org/en/latest/
.. _`flake8`: http://flake8.readthedocs.org/en/latest/
.. _`pyflakes`: https://github.com/pyflakes/pyflakes
.. _`pep8`: http://pep8.readthedocs.org/en/latest/

Continuous Integration
----------------------

The Meetup API test suite is exercised by Travis CI on every push
to the repo at GitHub. You can check out the current build status:
https://travis-ci.org/pferate/meetup-api

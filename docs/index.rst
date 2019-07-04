Welcome to Meetup API's documentation!
======================================

.. _Meetup: https://www.meetup.com/
.. _API: https://www.meetup.com/meetup_api/

.. Inline linking was needed here due to the apostrophe.

meetup-api is a Python client for `Meetup's <https://www.meetup.com/>`_ RESTful `API`_.  It is compatible with both Python 2 and Python 3.  Currently only OAuth token authentication is available, as Meetup is removing API Keys support on 15 August 2019.  The Python Requests-OAuthlib can be used to get OAuth tokens for this.

.. _user-docs:

.. toctree::
   :maxdepth: 3
   :caption: User Documentation

   getting_started

.. _package-docs:

.. toctree::
   :maxdepth: 2
   :caption: Package Information

   module_details

.. _dev-docs:

.. toctree::
   :maxdepth: 2
   :caption: Development Documentation

   tests
   changelog
   license

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`

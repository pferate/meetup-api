Getting Started
===============

This document will show you how to get up and running with the Meetup API Python Client.

Installation
------------

Meetup API requires the following packages installed:

- requests
- six

Assuming you have Python_ already, install the dependencies using ``pip``:

.. code-block:: bash

    $ cd /path/to/meetup-api
    $ pip install -r requirements.txt

Once the dependencies have been met, install the package:

.. code-block:: bash

    $ pip install meetup-api

Usage
-----

Initialize Client
~~~~~~~~~~~~~~~~~

To initialize your Meetup API Client, you will need to import the Client class and create a Client object. Before making and API requests, you will need to assign your API key to the object.

Three ways to assign your API key (in order of precedence):

1. Assign to attribute:

.. code-block:: python

    >>> import meetup.api
    >>> client = meetup.api.Client()
    >>> client.api_key = 'my_special_api_key_value'

2. Assign at initialization:

.. code-block:: python

    >>> import meetup.api
    >>> client = meetup.api.Client('my_special_api_key_value')

3. Retrieved from environment variable:

.. code-block:: bash

    $ export MEETUP_API_KEY=my_special_api_key_value

.. code-block:: python

    >>> import meetup.api
    >>> client = meetup.api.Client()

Execute API Calls
~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import meetup.api
    >>> client = meetup.api.Client('my_special_api_key_value')  
    >>> group_info = client.GetGroup({'urlname': 'Meetup-API-Testing'})
    >>> 
    >>> type(client)
    <class 'meetup.api.Client'>
    >>> 
    >>> type(group_info)
    <class 'meetup.api.MeetupObject'>
    >>> 
    >>> group_info.__dict__.keys()
    dict_keys(['who', 'join_mode', 'link', 'created', 'country', 'name', 'id', 'visibility',
               'state', 'urlname', 'city', 'lat', 'timezone', 'members', 'lon', 'description',
               'organizer', 'category', 'next_event', 'group_photo'])
    >>> 
    >>> group_info.id
    1556336
    >>> 
    >>> group_info.name
    'Meetup API Testing Sandbox'
    >>> 
    >>> group_info.link
    'http://www.meetup.com/Meetup-API-Testing/'

A full listing of implemented API methods can be found at
:ref:`meetup_api`.

.. _Python: https://www.python.org/


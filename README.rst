API Client for Meetup
=====================

|pypi-version| |build-status| |docs| |python-versions| |license|

A Python API client for Meetup_.

The official `Meetup REST API documentation`_ has a complete list of available API methods and their descriptions.  A listing of implemented API methods is documented at `API Client Details`_.

Quick Start
===============

For more information, take a look at the `Getting Started`_ section of the documentation.

Installation
------------

Assuming you have Python_ already, install the package using ``pip``:

.. code-block:: bash

    $ pip install meetup-api

Initialize Client and Execute API Call
--------------------------------------

.. code-block:: python

    >>> import meetup.api
    >>> client = meetup.api.Client('my_special_api_key_value')
    >>> 
    >>> type(client)
    <class 'meetup.api.Client'>
    >>> 
    >>> group_info = client.GetGroup({'urlname': 'Meetup-API-Testing'})
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

For a full listing of implemented API methods, take a look at the `API Client Details`_.

License
=======

The MIT License (MIT)

Copyright (c) 2016 Pat Ferate

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

.. _Meetup: http://www.meetup.com/
.. _Meetup REST API documentation: http://www.meetup.com/meetup_api/
.. _Python: https://www.python.org/
.. _API Client Details: http://meetup-api.readthedocs.org/en/latest/meetup_api.html#api-client-details
.. _Getting Started: http://meetup-api.readthedocs.org/en/latest/getting_started.html

.. |build-status| image:: https://img.shields.io/travis/pferate/meetup-api.svg?style=flat
    :alt: Build Status
    :scale: 100%
    :target: https://travis-ci.org/pferate/meetup-api

.. |docs| image:: https://readthedocs.org/projects/meetup-api/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://meetup-api.readthedocs.org/en/latest/?badge=latest

.. |pypi-version| image:: https://img.shields.io/pypi/v/meetup-api.svg
    :target: https://pypi.python.org/pypi/meetup-api/
    :alt: Latest Version
    :scale: 100%

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/meetup-api.svg
    :target: https://pypi.python.org/pypi/meetup-api/
    :alt: Python Versions
    :scale: 100%

.. |license| image:: https://img.shields.io/pypi/l/meetup-api.svg
    :target: https://pypi.python.org/pypi/meetup-api/
    :alt: License
    :scale: 100%

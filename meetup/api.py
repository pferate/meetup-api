from functools import partial
import json
import os
import requests
import six
from time import sleep

from meetup import exceptions


API_DEFAULT_URL = 'http://api.meetup.com/'
API_KEY_ENV_NAME = 'MEETUP_API_KEY'
API_SPEC_DIR = os.path.join(os.path.dirname(__file__), 'api_specification')
API_SERVICE_FILES = [
    ('v1', os.path.join(API_SPEC_DIR, 'meetup_v1_services.json')),
    ('v2', os.path.join(API_SPEC_DIR, 'meetup_v2_services.json')),
    ('v3', os.path.join(API_SPEC_DIR, 'meetup_v3_services.json')),
]
DEFAULT_WAIT_TIME = 30


class MeetupObjectList(list):
    """
    A custom, iterative list for MeetupObjects.

    Items are stored as raw, jsonified API Responses.  Items are converted to MeetupObjects on the fly.
    """
    def __init__(self, initial_list):
        self.items = initial_list

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return MeetupObject(self.items[key])

    def __iter__(self):
        for item in self.items:
            yield MeetupObject(item)


class MeetupObject(object):
    """
    Generic Meetup Object generated from dict and keyword arguments.

    Key/Values from dict are accessible from object as attributes (e.g. object.key)
    Keyword arguments passed at initialization are also accessible in the same way.
    Keyword values overwrite values from dict.

    :param initial_data: Initial values in a dict
    :param kwargs:       Additional key/values to set
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key, value in six.iteritems(dictionary):
                setattr(self, key, value)
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)


class RateLimit(object):
    """
    Rate limit information, as defined by Meetup.  This data is received in the response header.

    =========   =====================   =========================================================================
    Attribute   HTTP Header             Description
    =========   =====================   =========================================================================
    limit       X-RateLimit-Limit       The maximum number of requests that can be made in a window of time
    remaining   X-RateLimit-Remaining   The remaining number of requests allowed in the current rate limit window
    reset       X-RateLimit-Reset       The number of seconds until the current rate limit window resets
    =========   =====================   =========================================================================
    """

    limit = None
    remaining = None
    reset = None


class Client(object):
    """
    Meetup API Client.

    There are 3 options for defining the API key prior to making API calls:

    1. Pass it as a parameter (api_key)
    2. Stored as an environment variable, if parameter is not defined. (Default: MEETUP_API_KEY)
    3. Define it after the object is created. (client.api_key = 'my_secret_api_key')

    :param api_key:         Meetup API Key, from https://secure.meetup.com/meetup_api/key/
    :param api_url:         Meetup API URL,  Keeping it flexible so that it can be generalized in the future.
    :param overlimit_wait:  Whether or not to wait and retry if over API request limit. (Default: True)
    """

    def __init__(self, api_key=None, api_url=API_DEFAULT_URL, overlimit_wait=True):
        self._api_url = api_url
        self.api_key = api_key or os.environ.get(API_KEY_ENV_NAME)
        self.overlimit_wait = overlimit_wait
        self.session = requests.Session()
        self.rate_limit = RateLimit()
        # For internal references, can be refactored out if needed.
        self.services = {}
        # Not used at the moment, can be refactored out if needed.
        self._versioned_services = {}
        for version, file_name in API_SERVICE_FILES:
            api_data = json.load(open(file_name))
            self._versioned_services[version] = api_data
            for service_name, service_details in six.iteritems(api_data['operations']):
                # Call API Method directly as a class method
                self.__dict__[service_name] = partial(self._call, service_name)
                # API Method descriptions.  Used as a helpful reference.
                self.services[service_name] = service_details

    def _call(self, service_name, parameters=None, **kwargs):
        if not self.api_key:
            raise exceptions.ApiKeyError('Meetup API key not set')
        if not parameters:
            parameters = {}
        if not isinstance(parameters, dict):
            raise exceptions.ApiParameterError('Parameters must be dict')
        parameters['key'] = self.api_key
        for key, value in six.iteritems(kwargs):
            parameters[key] = value

        # Check for valid method
        if service_name not in self.services:
            raise exceptions.ApiMethodError('Unknown API Method [{0}]'.format(service_name))

        # Check for Required Parameters
        param_dict = self.services[service_name]['parameters']
        required_params = [k for k, v in six.iteritems(param_dict) if v['required']]
        for param_name in required_params:
            if not parameters.get(param_name):
                raise exceptions.ApiParameterError('Missing required parameter: {0}'.format(param_name))

        # Prepare API call parameters
        request_uri = self.services[service_name]['uri'].format(**parameters)
        request_url = '{0}{1}'.format(self._api_url, request_uri)
        request_http_method = self.services[service_name]['httpMethod']

        # Execute API Call
        # This can probably be simplified by calling `requests.request` directly,
        # but more testing will need to be done on parameters.
        if request_http_method == 'GET':
            response = self.session.get(request_url, params=parameters)
        elif request_http_method == 'POST':
            response = self.session.post(request_url, data=parameters)
        elif request_http_method == 'DELETE':
            response = self.session.delete(request_url, params=parameters)
        else:
            raise exceptions.HttpMethodError('HTTP Method not implemented: [{0}]'.format(request_http_method))

        # Update rate limit information
        self.rate_limit.limit = response.headers.get('X-RateLimit-Limit')
        self.rate_limit.remaining = response.headers.get('X-RateLimit-Remaining')
        self.rate_limit.reset = response.headers.get('X-RateLimit-Reset')
        print('{0}/{1} ({2} seconds remaining)'.format(self.rate_limit.remaining,
                                                       self.rate_limit.limit,
                                                       self.rate_limit.reset))

        if response.status_code == 401:
            raise exceptions.HttpUnauthorized
        if response.status_code == 404:
            raise exceptions.HttpNotFoundError

        # If we have two or less remaining calls in the period, wait (if the wait flag is set).
        # I tried only waiting after a 429 error, and ended getting locked out doing parallel testing.
        if int(self.rate_limit.remaining) <= 5 and self.overlimit_wait:
            if self.rate_limit.reset:
                sleep_time = 1 + int(self.rate_limit.reset)
            else:
                sleep_time = DEFAULT_WAIT_TIME
            print('Sleeping for {0} seconds'.format(sleep_time))
            sleep(sleep_time)

        if response.status_code == 429:
            if self.overlimit_wait:
                # We should have already waited
                self._call(service_name, parameters)
            else:
                raise exceptions.HttpTooManyRequests(response.content)

        jsonified = response.json()
        if isinstance(jsonified, list):
            return MeetupObjectList(jsonified)
        else:
            return MeetupObject(jsonified)

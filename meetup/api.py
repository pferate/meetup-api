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


class MeetupObject(object):
    """
    Generic Meetup Object generated from dict and keyword arguments.
    """
    def __init__(self, *initial_data, **kwargs):
        """
        Key/Values from dict are accessible from object as attributes (e.g. object.key)
        Keyword arguments passed at initialization are also accessible in the same way.
        Keyword values overwrite values from dict.

        :param initial_data Initial values in a dict
        :param kwargs       Additional key/values to set
        """
        for dictionary in initial_data:
            for key, value in six.iteritems(dictionary):
                setattr(self, key, value)
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)


class RateLimit(object):
    """
    Rate limit information, as defined by Meetup.  This data is received in the response header.
    limit       X-RateLimit-Limit       The maximum number of requests that can be made in a window of time
    remaining   X-RateLimit-Remaining   The remaining number of requests allowed in the current rate limit window
    reset       X-RateLimit-Reset       The number of seconds until the current rate limit window resets
    """
    limit = None
    remaining = None
    reset = None


class Client(object):
    """
    Meetup API Client.

    """

    def __init__(self, api_key=None, api_url=API_DEFAULT_URL, overlimit_wait=False):
        """
        There are 3 options for defining the API key prior to making API calls:
        1. Pass it as a parameter (api_key)
        2. Stored as an environment variable, if parameter is not defined. (Default: MEETUP_API_KEY)
        3. Define it after the object is created. (client.api_key = 'my_secret_api_key')

        :param api_key:         Meetup API Key, from https://secure.meetup.com/meetup_api/key/
        :param api_url:         Meetup API URL,  Keeping it flexible so that it can be generalized in the future.
        :param overlimit_wait:  Whether or not to wait and retry if over API request limit. (Default: False)
        """
        self._api_url = api_url
        self.api_key = api_key or os.environ.get(API_KEY_ENV_NAME)
        self.overlimit_wait = overlimit_wait
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

    def _call(self, service_name, parameters=None):
        if not self.api_key:
            raise exceptions.ApiKeyError('Meetup API key not set')
        if not isinstance(parameters, dict):
            raise exceptions.ApiParameterError('Parameters must be dict')
        if not parameters:
            parameters = {}
        parameters['key'] = self.api_key

        # Check for valid method
        if service_name not in self.services:
            raise exceptions.ApiMethodError('Unknown API Method [{}]'.format(service_name))

        # Check for Required Parameters
        param_dict = self.services[service_name]['parameters']
        required_params = [k for k, v in six.iteritems(param_dict) if v['required']]
        for param_name in required_params:
            if not parameters.get(param_name):
                raise exceptions.ApiParameterError('Missing required parameter: {}'.format(param_name))

        # Prepare API call parameters
        request_uri = self.services[service_name]['uri'].format(**parameters)
        request_url = '{}{}'.format(self._api_url, request_uri)
        request_http_method = self.services[service_name]['httpMethod']

        # Execute API Call
        # This can probably be simplified by calling `requests.request` directly,
        # but more testing will need to be done on parameters.
        if request_http_method == 'GET':
            response = requests.get(request_url, params=parameters)
        elif request_http_method == 'POST':
            response = requests.post(request_url, data=parameters)
        elif request_http_method == 'DELETE':
            response = requests.delete(request_url, params=parameters)
        else:
            raise exceptions.HttpMethodError('HTTP Method not implemented: [{}]'.format(request_http_method))

        # Update rate limit information
        self.rate_limit.limit = response.headers.get('X-RateLimit-Limit')
        self.rate_limit.remaining = response.headers.get('X-RateLimit-Remaining')
        self.rate_limit.reset = response.headers.get('X-RateLimit-Reset')

        if response.status_code == 401:
            raise exceptions.HttpUnauthorized
        if response.status_code == 404:
            raise exceptions.HttpNotFoundError
        if response.status_code == 429:
            if self.overlimit_wait:
                sleep(self.rate_limit.reset)
                self._call(service_name, parameters)
            else:
                raise exceptions.HttpTooManyRequests

        return MeetupObject(response.json())

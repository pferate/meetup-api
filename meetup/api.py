from functools import partial
import json
import os
import requests
import six

from meetup import API_DEFAULT_URL, API_KEY_ENV_NAME, API_SERVICE_FILES, MeetupObject
from meetup.exceptions import ApiKeyError, ApiMethodError, ApiParameterError, \
    HttpMethodError, HttpNotFoundError, HttpUnauthorized, HttpTooManyRequests


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

    def __init__(self, api_key=None, api_url=API_DEFAULT_URL):
        """
        There are 3 options for defining the API key prior to making API calls:
        1. Pass it as a parameter (api_key)
        2. Stored as an environment variable, if parameter is not defined. (Default: MEETUP_API_KEY)
        3. Define it after the object is created. (client.api_key = 'my_secret_api_key')

        :param api_key: Meetup API Key, from https://secure.meetup.com/meetup_api/key/
        :param api_url: Meetup API URL,  Keeping it flexible so that it can be generalized in the future.
        """
        self._api_url = api_url
        self.api_key = api_key or os.environ.get(API_KEY_ENV_NAME)
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
            raise ApiKeyError('Meetup API key not set')
        if not isinstance(parameters, dict):
            raise ApiParameterError('Parameters must be dict')
        if not parameters:
            parameters = {}
        parameters['key'] = self.api_key

        # Check for valid method
        if service_name not in self.services:
            raise ApiMethodError('Unknown API Method [{}]'.format(service_name))

        # Check for Required Parameters
        param_dict = self.services[service_name]['parameters']
        required_params = [k for k, v in six.iteritems(param_dict) if v['required']]
        for param_name in required_params:
            if not parameters.get(param_name):
                raise ApiParameterError('Missing required parameter: {}'.format(param_name))

        # Prepare API call parameters
        request_uri = self.services[service_name]['uri'].format(**parameters)
        request_url = '{}{}'.format(self._api_url, request_uri)
        request_http_method = self.services[service_name]['httpMethod']

        # Execute API Call
        # This can probably be simplified by calling `requests.request` directly,
        # but more testing will need to be done on parameters.
        if request_http_method == 'GET':
            result = requests.get(request_url, params=parameters)
        elif request_http_method == 'POST':
            result = requests.post(request_url, data=parameters)
        elif request_http_method == 'DELETE':
            result = requests.delete(request_url, params=parameters)
        else:
            raise HttpMethodError('HTTP Method not implemented: [{}]'.format(request_http_method))

        # Update rate limit information
        self.rate_limit.limit = result.headers.get('X-RateLimit-Limit')
        self.rate_limit.remaining = result.headers.get('X-RateLimit-Remaining')
        self.rate_limit.reset = result.headers.get('X-RateLimit-Reset')

        if result.status_code == 401:
            raise HttpUnauthorized
        if result.status_code == 404:
            raise HttpNotFoundError
        if result.status_code == 429:
            raise HttpTooManyRequests

        return MeetupObject(result.json())

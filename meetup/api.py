from functools import partial
import json
import os
import requests
import six

from meetup import API_DEFAULT_URL, API_KEY_ENV_NAME, API_SERVICE_FILES
from meetup.exceptions import ApiKeyError, ApiMethodError, ApiParameterError, HttpMethodError


class Client(object):

    def __init__(self, api_key=None, api_url=API_DEFAULT_URL):
        self._api_url = api_url
        # Set the API key on initialization, from environment variable, or overwritten later
        self.api_key = api_key or os.environ.get(API_KEY_ENV_NAME)
        # For internal references, can be refactored out if needed.
        self.services = {}
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

        # Execute API Call
        request_uri =  self.services[service_name]['uri'].format(**parameters)
        request_url = '{}{}'.format(self._api_url, request_uri)
        request_http_method = self.services[service_name]['httpMethod']
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

        return result

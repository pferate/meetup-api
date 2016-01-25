from functools import partial
import json
import os
import six
import slumber

from meetup import API_DEFAULT_URL, API_KEY_ENV_NAME, API_SERVICE_FILES
from meetup.exceptions import ApiKeyException, ApiMethodNotDefined


class Client(object):

    def __init__(self, api_key=None, api_url=API_DEFAULT_URL):
        self._api = slumber.API(api_url)
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
            raise ApiKeyException('Meetup API key not set')
        print(service_name)
        print(parameters)
        print('Calling [{}] with the parameters: [{}]'.format(service_name, parameters))
        if service_name not in self.services:
            raise ApiMethodNotDefined('Unknown API Method [{}]'.format(service_name))
        print(self.services[service_name])

import json
import os
import six
import slumber

from meetup import API_DEFAULT_URL, API_KEY_ENV_NAME, API_SERVICE_FILES
from meetup.exceptions import ApiKeyException, ApiMethodNotDefined


class Client(object):

    def __init__(self, api_key=None, api_url=API_DEFAULT_URL):
        self.api = slumber.API(api_url)
        # Set the API key on initialization, from environment variable, or overwritten later
        self.api_key = api_key or os.environ.get(API_KEY_ENV_NAME)
        self.services = {
            'all': {}
        }
        for version, file_name in six.iteritems(API_SERVICE_FILES):
            api_data = json.load(open(file_name))
            self.services[version] = api_data
            self.services['all'] = api_data['operations']

    def call(self, service_name, parameters):
        if not self.api_key:
            raise ApiKeyException('Meetup API key not set')
        print(service_name)
        print(parameters)
        print('Calling [{}] with the parameters: [{}]'.format(service_name, parameters))
        if service_name not in self.services['all']:
            raise ApiMethodNotDefined('Unknown API Method [{}]'.format(service_name))
        print(self.services['all'][service_name])

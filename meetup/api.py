import json
import os
import six
import slumber

from meetup.exceptions import ApiKeyException, ApiMethodNotDefined


API_DEFAULT_URL = 'http://api.meetup.com/'
API_KEY_ENV_NAME = 'MEETUP_API_KEY'
CONFIG_DIR = os.path.join(os.path.dirname(__file__), 'config')
API_SERVICE_FILES = {
    'v1': os.path.join(CONFIG_DIR, 'meetup_v1_services.json'),
    'v2': os.path.join(CONFIG_DIR, 'meetup_v2_services.json'),
    'v3': os.path.join(CONFIG_DIR, 'meetup_v3_services.json'),
}


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

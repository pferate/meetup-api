import os
import six


API_DEFAULT_URL = 'http://api.meetup.com/'
API_KEY_ENV_NAME = 'MEETUP_API_KEY'
CONFIG_DIR = os.path.join(os.path.dirname(__file__), 'config')
API_SERVICE_FILES = [
    ('v1', os.path.join(CONFIG_DIR, 'meetup_v1_services.json')),
    ('v2', os.path.join(CONFIG_DIR, 'meetup_v2_services.json')),
    ('v3', os.path.join(CONFIG_DIR, 'meetup_v3_services.json')),
]


class MeetupObject(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key, value in six.iteritems(dictionary):
                setattr(self, key, value)
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)

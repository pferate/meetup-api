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


class BaseFromDictClass(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key, value in six.iteritems(dictionary):
                setattr(self, key, value)
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)


class Group(BaseFromDictClass):
    """
    Class for Meetup API 'groups' endpoints.  Only v3 endpoints are available at the moment.
    Currently GET is the only HTTP Method available.
    """
    # TODO: Add method and parameter documentation
    # TODO: Explicitly expand **kwargs
    # TODO: Add other HTTP Method functions

    def __init__(self, *initial_data, **kwargs):
        """Meetup groups class.

        :param initial_data: Information about group in dict format

        """
        super().__init__(*initial_data, **kwargs)

import os
import six
import slumber

API_KEY = os.environ.get('MEETUP_API_KEY')

API_URL = 'http://api.meetup.com/'

API = slumber.API(API_URL)


class BaseFromDictClass(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key, value in six.iteritems(dictionary):
                setattr(self, key, value)
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)

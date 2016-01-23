import six

from meetup import api


class BaseFromDictClass(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key, value in six.iteritems(dictionary):
                setattr(self, key, value)
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)

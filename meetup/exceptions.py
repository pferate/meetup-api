
class MeetupBaseException(Exception):
    """
    All Meetup exceptions inherit from this exception.
    """


class MeetupClientException(MeetupBaseException):
    """
    Meetup Client Exception base class.
    """


class ApiKeyException(MeetupClientException):
    """
    There is a problem with the client API key.
    """


class ApiMethodNotDefined(MeetupClientException):
    """
    The called API method is not defined or does not exist.
    """

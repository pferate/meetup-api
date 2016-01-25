
class MeetupBaseException(Exception):
    """
    All Meetup exceptions inherit from this exception.
    """


class ClientException(MeetupBaseException):
    """
    Meetup Client Exception base class.
    """


class ApiKeyError(ClientException):
    """
    There is a problem with the client API key.
    """


class ApiMethodError(ClientException):
    """
    The called API method is not defined or does not exist.
    """


class ApiParameterError(ClientException):
    """
    The called API method is missing a required parameter.
    """


class HttpMethodError(ClientException):
    """
    The requested HTTP Method is not valid.
    """

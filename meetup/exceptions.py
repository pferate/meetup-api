class MeetupBaseException(Exception):
    """
    All Meetup exceptions inherit from this exception.
    """


class ClientException(MeetupBaseException):
    """
    Meetup Client Exception base class.
    """


class TokenError(ClientException):
    """
    There is a problem with the client OAuth token.
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


class MeetupHttpBaseException(MeetupBaseException):
    """
    All Meetup HTTP Exceptions inherit from this exception.
    """


class HttpClientError(MeetupHttpBaseException):
    """
    Called when the server tells us there was a client error (4xx).
    """


class HttpUnauthorized(HttpClientError):
    """
    Called when the server sends a 401 error (when you don't provide a valid OAuth token)
    """


class HttpNotFoundError(HttpClientError):
    """
    Called when the server sends a 404 error.
    """


class HttpNotAccessibleError(HttpClientError):
    """
    Called when the server sends a 410 error.
    """


class HttpTooManyRequests(HttpClientError):
    """
    Called when the server sends a 429 error (when you've gone over your request rate limit)
    """


class HttpServerError(MeetupHttpBaseException):
    """
    Called when the server tells us there was a server error (5xx).
    """

import os
import pytest

from meetup import exceptions
from meetup.api import TOKEN_ENV_NAME, Client, MeetupObject


@pytest.fixture
def api_client():
    return Client()


@pytest.mark.incremental
class TestToken:
    def test_environment_key(self, api_client):
        # Compare object OAuth token with environment variable
        assert api_client.token == os.environ.get(TOKEN_ENV_NAME)

    def test_empty_key(self, api_client):
        # Undefined OAuth token should fail
        api_client.token = None
        with pytest.raises(exceptions.TokenError):
            api_client.GetDashboard()

    def test_invalid_key(self, api_client):
        # Same with invalid API Key
        api_client.token = 'foobarbaz'
        with pytest.raises(exceptions.HttpUnauthorized):
            api_client.GetDashboard()


@pytest.mark.incremental
class TestApiParameters:
    def test_non_dict(self, api_client):
        # Parameter needs to be a dict
        with pytest.raises(exceptions.ApiParameterError):
            api_client.GetDashboard('foobarbaz')

    def test_non_required(self, api_client):
        # If a parameter is not required, passing no parameter should be okay
        assert isinstance(api_client.GetDashboard(), MeetupObject)

    def test_empty_dict(self, api_client):
        # Same with an empty dict
        assert isinstance(api_client.GetDashboard({}), MeetupObject)

    def test_missing_required(self, api_client):
        # But if a parameter is required, passing no parameter should fail
        with pytest.raises(exceptions.ApiParameterError):
            api_client.GetGroup()

    def test_empty_required(self, api_client):
        # Same with an empty dict
        with pytest.raises(exceptions.ApiParameterError):
            api_client.GetGroup({})


@pytest.mark.incremental
class TestApiMethods:
    def test_invalid_methods(self, api_client):
        # Invalid method names should not be an attribute
        with pytest.raises(AttributeError):
            api_client.FooBarBaz()

    def test_invalid_service(self, api_client):
        # If we add the method without adding the associated service, it should fail
        from functools import partial
        api_client.FooBarBaz = partial(api_client._call, 'FooBarBaz')
        with pytest.raises(exceptions.ApiMethodError):
            api_client.FooBarBaz()

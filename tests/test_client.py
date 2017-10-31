import os
import pytest
from requests import HTTPError

from meetup import exceptions
from meetup.api import API_KEY_ENV_NAME, Client, MeetupObject


@pytest.fixture
def api_client():
    return Client()


@pytest.mark.incremental
class TestApiKey:
    def test_environment_key(self, api_client):
        # Compare object API key with environment variable
        assert api_client.api_key == os.environ.get(API_KEY_ENV_NAME)

    def test_empty_key(self, api_client):
        # Undefined API Key should fail
        api_client.api_key = None
        with pytest.raises(exceptions.ApiKeyError):
            api_client.GetDashboard()

    def test_invalid_key(self, api_client):
        # Same with invalid API Key
        api_client.api_key = 'foobarbaz'
        with pytest.raises(HTTPError) as excinfo:
            api_client.GetDashboard()
        assert '401 Client Error' in str(excinfo.value)


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

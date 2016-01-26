import pytest

from meetup import exceptions
from meetup.api import MeetupObject


valid_groups = ['Meetup-API-Testing', 'PSPPython', 'Seattle-Data-Science', 'codefellows']
invalid_groups = ['foobarbaz', '-', '123']


@pytest.fixture
def api_client():
    import meetup.api
    return meetup.api.Client()


@pytest.mark.parametrize("group_name", valid_groups)
def test_get_valid_group(api_client, group_name):
    group_info = api_client.GetGroup({'urlname': group_name})
    assert isinstance(group_info, MeetupObject)


@pytest.mark.parametrize("group_name", invalid_groups)
def test_get_invalid_group(api_client, group_name):
    with pytest.raises(exceptions.HttpNotFoundError):
        api_client.GetGroup({'urlname': group_name})


@pytest.mark.parametrize("group_name", valid_groups)
def test_case_insensitive_group_name(api_client, group_name):
    group = api_client.GetGroup({'urlname': group_name})
    group_lower = api_client.GetGroup({'urlname': group_name.lower()})
    group_upper = api_client.GetGroup({'urlname': group_name.upper()})
    assert isinstance(group, MeetupObject)
    assert isinstance(group_lower, MeetupObject)
    assert isinstance(group_upper, MeetupObject)
    assert group.id == group_lower.id == group_upper.id
    assert group.name == group_lower.name == group_upper.name

import pytest

from meetup.api import Client, MeetupObject, MeetupObjectList


@pytest.fixture
def api_client():
    return Client()


def test_get_find_groups(api_client):
    find_group_info = api_client.GetFindGroups()
    assert isinstance(find_group_info, MeetupObjectList)
    assert isinstance(find_group_info[0], MeetupObject)
    assert isinstance(find_group_info[-1], MeetupObject)

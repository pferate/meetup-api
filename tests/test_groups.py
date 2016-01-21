import pytest
from slumber.exceptions import HttpNotFoundError

from meetup import groups


valid_groups = ['Meetup-API-Testing', 'PSPPython', 'Seattle-Data-Science', 'codefellows']
invalid_groups = ['foobarbaz', '-', '123']


@pytest.mark.parametrize("group_name", valid_groups)
def test_get_valid_group(group_name):
    group_info = groups.get(group_name)
    # print(group_info)
    assert isinstance(group_info, dict)


@pytest.mark.parametrize("group_name", invalid_groups)
def test_get_invalid_group(group_name):
    with pytest.raises(HttpNotFoundError):
        groups.get(group_name)
import pytest
from slumber.exceptions import HttpNotFoundError

from meetup import groups


valid_groups = ['Meetup-API-Testing', 'PSPPython', 'Seattle-Data-Science', 'codefellows']
invalid_groups = ['foobarbaz', '-', '123']


@pytest.mark.parametrize("group_name", valid_groups)
def test_get_valid_group(group_name):
    group_info = groups.get(group_name)
    assert isinstance(group_info, groups.Group)


@pytest.mark.parametrize("group_name", invalid_groups)
def test_get_invalid_group(group_name):
    with pytest.raises(HttpNotFoundError):
        groups.get(group_name)


@pytest.mark.parametrize("group_name", valid_groups)
def test_case_insensitive_group_name(group_name):
    group = groups.get(group_name)
    group_lower = groups.get(group_name.lower())
    group_upper = groups.get(group_name.upper())
    assert group.id == group_lower.id == group_upper.id
    assert group.name == group_lower.name == group_upper.name
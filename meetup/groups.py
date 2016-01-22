"""
Modules for Meetup API 'groups' endpoints.
Only v3 endpoints are available at the moment.
Currently GET is the only HTTP Method available.

v3 Endpoints:
    * GET /find/groups
    * GET /:urlname
    * POST /:urlname
    * POST /:urlname/topics
    * DELETE /:urlname/topics
    * GET /recommended/groups
    * POST /recommended/groups/ignores/:urlname
    * GET /:urlname/similar_groups
"""
# TODO: Add method and parameter documentation
# TODO: Explicitly expand **kwargs
# TODO: Add other HTTP Method functions

from meetup import API, API_KEY, BaseFromDictClass


class Group(BaseFromDictClass):
    """
    Class for Meetup API 'groups' endpoints.  Only v3 endpoints are available at the moment.
    Currently GET is the only HTTP Method available.
    """
    # TODO: Add method and parameter documentation
    # TODO: Explicitly expand **kwargs
    # TODO: Add other HTTP Method functions

    def __init__(self, *initial_data, **kwargs):
        """Meetup groups class.

        :param initial_data: Information about group in dict format

        """
        super().__init__(*initial_data, **kwargs)


def find(**kwargs):
    """Find Meetup groups.

    Using a staticmethod instead of classmethod to maintain object type as Group.

    :param category:              Comma-delimited list of numeric category ids
    :type category: str
    :param country:               A valid two character country code, defaults to US
    :type country: str
    :param fallback_suggestions:  boolean indicator of whether or not to return a list of curated suggestions for groups if we can't find groups matching your criteria
    :type fallback_suggestions: str
    :param fields:                Request that additional fields (separated by commas) be included in the output.
    :type fields: str
    :param filter:                Determines which groups are returned. If 'all' (default), the text and category parameters are applied. If 'friends', groups your friends are in are returned. The value of this parameter may be one of all, friends
    :type filter: str
    :param lat:                   Approximate latitude
    :type lat: str
    :param location:              Raw text location query
    :type location: str
    :param lon:                   Approximate longitude
    :type lon: str
    :param radius:                Radius in miles. May be 0.0-100.0, 'global' or 'smart', a dynamic radius based on the number of active groups in the area. Defaults to member's preferred radius
    :type radius: str
    :param self_groups:           set to 'include' or 'exclude' Meetups the authorized member belongs to; default is 'include'
    :type self_groups: str
    :param text:                  Raw full text search query
    :type text: str
    :param topic_id:              Comma-delimited list of numeric topic ids
    :type topic_id: str
    :param upcoming_events:       If true, filters text and category based searches on groups that have upcoming events. Defaults to false
    :type upcoming_events: str
    :param zip:                   Zipcode of location to limit search to
    :type zip: str
    :returns: list -- List of matching groups

    """
    return [Group(data) for data in API.find.groups.get(key=API_KEY, **kwargs)]


def get(group_name, **kwargs):
    return Group(API.__getattr__(group_name).get(key=API_KEY, **kwargs))


def recommended(**kwargs):
    return [Group(data) for data in API.recommended.groups.get(key=API_KEY, **kwargs)]


def similar(group_name, **kwargs):
    return [Group(data) for data in API.__getattr__(group_name).similar_groups.get(key=API_KEY, **kwargs)]

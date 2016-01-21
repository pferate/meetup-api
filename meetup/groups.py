"""
Modules for Meetup API 'groups' endpoints.
Only v3 endpoints are available at the moment.
Currently GET is the only HTTP Method available.

Endpoints:
    GET /find/groups
    GET /:urlname
    POST /:urlname
    POST /:urlname/topics
    DELETE /:urlname/topics
    GET /recommended/groups
    POST /recommended/groups/ignores/:urlname
    GET /:urlname/similar_groups
"""
# TODO: Add method and parameter documentation
# TODO: Explicitly expand **kwargs
# TODO: Add other HTTP Method functions

from meetup import API, API_KEY


def find(**kwargs):
    return API.find.groups.get(key=API_KEY, **kwargs)


def get(group_name, **kwargs):
    return API.__getattr__(group_name).get(key=API_KEY, **kwargs)


def recommended(**kwargs):
    return API.find.recommended.get(key=API_KEY, **kwargs)


def similar(group_name, **kwargs):
    return API.__getattr__(group_name).similar_groups.get(key=API_KEY, **kwargs)

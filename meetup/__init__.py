import os
import six


API_DEFAULT_URL = 'http://api.meetup.com/'
API_KEY_ENV_NAME = 'MEETUP_API_KEY'
API_SPEC_DIR = os.path.join(os.path.dirname(__file__), 'api_specification')
API_SERVICE_FILES = [
    ('v1', os.path.join(API_SPEC_DIR, 'meetup_v1_services.json')),
    ('v2', os.path.join(API_SPEC_DIR, 'meetup_v2_services.json')),
    ('v3', os.path.join(API_SPEC_DIR, 'meetup_v3_services.json')),
]

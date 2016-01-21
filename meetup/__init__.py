import os
import slumber

API_KEY = os.environ.get('MEETUP_API_KEY')

API_URL = 'http://api.meetup.com/'

API = slumber.API(API_URL)

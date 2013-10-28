import os

from google.appengine.dist import use_library
use_library('django', '1.2')
os.environ['DJANGO_SETTINGS_MODULE'] = '__init__'

import webapp2 as webapp

urls = [
]

app = webapp.WSGIApplication(urls, debug=True)

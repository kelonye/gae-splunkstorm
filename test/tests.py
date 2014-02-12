import os
import sys
sys.path.insert(0, '/usr/local/google_appengine')
import dev_appserver
dev_appserver.fix_sys_path()

from google.appengine.ext import testbed
from views import app
import unittest
import webtest
import logging
from lib import splunk

logger = logging.getLogger(__name__)


class TestCase(unittest.TestCase):

    def setUp(self):

        self.app = webtest.TestApp(app)

        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_urlfetch_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_post(self):

        splunk.access_token = ''
        splunk.project_id = ''

        logger.log({
          'event': 'event',
          'duration': '5ms'
        })

        # TODO: more test

unittest.main()
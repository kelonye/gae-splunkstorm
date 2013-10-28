#!/usr/bin/env python

import urllib
import base64
from google.appengine.api import urlfetch
from google.appengine._internal.django.utils import simplejson as json


INPUT_URL = 'https://api.splunkstorm.com/1/inputs/http?'


class Log(object):

    def __init__(
        self,
        access_token,
        project_id,
        input_url=INPUT_URL
    ):

        self.input_url = input_url
        self.project_id = project_id
        self.access_token = access_token

    def send(
        self,
        event_json,
        sourcetype='syslog',
        host=None,
        source=None
    ):

        params = {
            'project': self.project_id,
            'sourcetype': sourcetype
        }
        if host:
            params['host'] = host
        if source:
            params['source'] = source

        url = self.input_url + urllib.urlencode(params)

        payload = json.dumps(event_json)

        authorization = 'Basic ' + base64.b64encode(':'+self.access_token)
        headers = {'Authorization': authorization}

        # rpc = urlfetch.create_rpc()
        # urlfetch.make_fetch_call(
        #     rpc,
        #     url,
        #     payload=payload,
        #     headers=headers,
        #     method=urlfetch.POST
        # )
        # rpc.get_result()

        return urlfetch.fetch(
            url,
            payload=payload,
            headers=headers,
            method=urlfetch.POST
        )
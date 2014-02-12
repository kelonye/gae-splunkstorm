#!/usr/bin/env python

import urllib
import base64
from google.appengine.api import urlfetch
from google.appengine._internal.django.utils import simplejson as json


input_url = 'https://api.splunkstorm.com/1/inputs/http?'
project_id = None
access_token = None


def log(
    event_json,
    sourcetype='syslog',
    host=None,
    source=None
):


    """ posts to input_url

        Args:
            event_json{dict} - event payload
            sourcetype{str} - sourcetype,  defaults to syslog
            host{str} - log host origin host
            source{str} - log origin api

        Returns:
            {str} - post response
        
    """

    if not project_id:
        raise Exception('project_id is required')
    if not access_token:
        raise Exception('access_token is required')

    params = {
        'project': project_id,
        'sourcetype': sourcetype
    }
    if host:
        params['host'] = host
    if source:
        params['source'] = source

    url = input_url + urllib.urlencode(params)

    payload = json.dumps(event_json)

    authorization = 'Basic ' + base64.b64encode(':'+access_token)
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
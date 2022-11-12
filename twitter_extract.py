#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:47:03 2022

@author: rishabhpatni
"""

import requests



BEARER_TOKEN = ""



def connect_to_twitter():
    return {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r



def search_twitter(query_params):

    url = "https://api.twitter.com/2/tweets/search/all"

    response = requests.request("GET", url, auth=bearer_oauth, params = query_params)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

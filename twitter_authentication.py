#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:47:03 2022

@author: rishabhpatni
"""
import requests

# sends API request with given query parameters, returns response in json format 
def search_twitter(query_params, bearer_token):

    url = "https://api.twitter.com/2/tweets/search/all"
    bearer_oauth = {"Authorization": f"Bearer {bearer_token}", "User-Agent":"v2TweetLookupPython" }
    response = requests.request("GET", url, params = query_params, headers = bearer_oauth)
    response.headers["Authorization"] = f"Bearer {bearer_token}"
    response.headers["User-Agent"] = "v2TweetLookupPython"

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

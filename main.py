#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:56:55 2022

@author: rishabhpatni
"""

from twitter_extract import search_twitter
import json

query = "climate change"
max_results = 10

query_params = {'query': query,'tweet.fields': 'text', 'max_results': max_results}



def main():
    json_response = search_twitter(query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))

    
main()
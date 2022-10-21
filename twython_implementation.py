#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:24:49 2022

@author: rishabhpatni
"""

from twython import Twython

APP_KEY = ''
ACCESS_TOKEN = ''

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

results = twitter.search(q='climate change', count=5)

all_tweets = results['statuses']

i= 0
for tweet in all_tweets:
    i += 1
    print(tweet['text'][:20])
    print(i)

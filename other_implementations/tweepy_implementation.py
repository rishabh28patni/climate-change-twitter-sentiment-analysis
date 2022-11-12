#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:40:55 2022

@author: rishabhpatni
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:24:49 2022

@author: rishabhpatni
"""

'''
Accessing twitter API using tweepy library. This works with the recent-search endpoint
to get recent tweets given a query. 
'''

! pip install tweepy
import tweepy

ACCESS_TOKEN = ""           # include personal access token from twitter API
auth = tweepy.Client(ACCESS_TOKEN)
api = tweepy.API(auth)

query = "climate change"


response  = auth.search_recent_tweets(query, max_results = 10)

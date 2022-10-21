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

import tweepy

ACCESS_TOKEN = ""
auth = tweepy.Client(ACCESS_TOKEN)
api = tweepy.API(auth)

query = "climate change"


response  = auth.search_recent_tweets(query, max_results = 10)

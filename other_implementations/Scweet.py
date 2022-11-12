#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:27:27 2022

@author: rishabhpatni
"""

'''
Accessing twitter API using Scweet library. 
'''

!pip install Scweet==1.8

from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

words1 = ["climate change", "carbon dioxide", "fossil fuel", 
          "carbon footprint", "emissions", "global warming", "greenhouse gases"]

data = scrape(words=words1, since="2021-01-01", until="2021-12-31", from_account = None,        
              interval=1, headless=False, display_type="Top", save_images=False, lang="en",
	resume=False, filter_replies=True, proximity=False, geocode=True)



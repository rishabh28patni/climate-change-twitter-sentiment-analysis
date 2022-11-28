#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 22:30:25 2022

@author: rishabhpatni
"""
import API_data_extraction
import tweet_processing


# Parameters to set

# Query parameters as defined in https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#build
query = 'has:geo -is:retweet -is:nullcast (place_country:US) ("climate change" OR "carbon dioxide" OR "fossil fuel" OR "carbon footprint" OR emissions OR "global warming" OR "greenhouse gases") lang:en' 
start_date = '2020-01-01T00:00:00Z'
end_date = '2022-01-01T00:00:00Z'
max_tweets = 500
location = ""
## Bearer token given by twitter API to access endpoints
bearer_token = ""
#flag for if we need to run query. if false, then just processes data in /data_output/
generate_data = True

def main():
    if generate_data: 
        API_data_extraction.get_tweets(query=query, start_date = start_date, end_date= end_date,
                                       max_tweets=max_tweets, bearer_token = bearer_token, location = location)
    tweet_processing.data_processing()
    
main()

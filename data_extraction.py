#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:56:55 2022

@author: rishabhpatni
"""

from twitter_extract import search_twitter
import pandas as pd 
from time import sleep



query1 = 'has:geo -is:retweet -is:nullcast (place_country:IN OR place_country:PK OR place_country:LK OR place_country:BD OR place_country:NP OR place_country:BT) ("climate change" OR "carbon dioxide" OR "fossil fuel" OR "carbon footprint" OR emissions OR "global warming" OR "greenhouse gases") lang:en' 
max_results = 500
start_date = '2020-01-01T00:00:00Z'
end_date = '2022-01-01T00:00:00Z'
tweets_counter = 500
location = "South_Asia"

query_params = {
    "query": query1,
    "start_time": start_date,
    "end_time": end_date,
    "max_results": max_results,
    "tweet.fields": 
        "geo,public_metrics,created_at",
    "expansions": 
            "geo.place_id", 
    "place.fields": 
        "contained_within,country,country_code,full_name,geo,id,name",
    "user.fields": 
        "created_at,name"#,
    #'sort_order':
    #    "recency"
  }



def running(tweets_counter):
    final_results = pd.DataFrame(columns = ["text", "created_at", "like_count", "retweet_count", "reply_count", "geo_place_id",
                                            "country_code", "country", "name", "full_name", "bbox"])
    count = 0
    counter = 0
    json_response = search_twitter(query_params)

    
    while (('next_token' in json_response['meta']) and ('data' in json_response) and (counter <= tweets_counter)):
        sleep(5)
        count += 1
        json_response = search_twitter(query_params)
        
        if ('data' not in json_response):
            break
    
        df = pd.DataFrame(json_response["data"])
        print(df.shape)
        df = df.dropna()
        df["retweet_count"] = df["public_metrics"].apply(lambda row: row["retweet_count"])
        df["reply_count"] = df["public_metrics"].apply(lambda row: row["reply_count"])
        df["like_count"] = df["public_metrics"].apply(lambda row: row["like_count"])
        df["geo_place_id"] = df["geo"].apply(lambda row: row["place_id"])
        df = df[["text", "created_at", "like_count", "retweet_count", "reply_count", "geo_place_id"]]
        
        counter += df.shape[0]
        print(counter)
        
        
        
        df2 = pd.DataFrame(json_response["includes"]["places"])
        df2 = df2.dropna()
        df2["bbox"] = df2["geo"].apply(lambda row: row["bbox"])
        df2=df2[["id", "country_code", "country", "name", "full_name", "bbox"]]
        df2.columns = ["geo_place_id", "country_code", "country", "name", "full_name", "bbox"]
        
        
        combined = pd.merge(df, df2, how = 'inner', on = 'geo_place_id')
        print(combined.shape)
        print('\n')
        final_results = pd.concat([final_results, combined], ignore_index= True)
        
        if ('next_token' not in json_response['meta']):
            break
        
        query_params["next_token"] = json_response["meta"]["next_token"]
    
    final_results.to_csv(f'data_output/final_{location}.csv')

    return final_results
    

final = running(tweets_counter)

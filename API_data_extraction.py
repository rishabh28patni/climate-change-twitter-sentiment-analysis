#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:56:55 2022

@author: rishabhpatni
"""

from twitter_authentication import search_twitter
import pandas as pd 
from time import sleep

def get_tweets(query, start_date, end_date, max_tweets, location, bearer_token, results_per_request = 500):
    '''
    Parameters
    ----------
    max_tweets : Integer
        DESCRIPTION. number of tweets we would want to query. 

    Returns
    -------
    final_results : DataFrame
        dataframe giving tweets and other information.

    '''
    # build query dictionary from inputs
    query_params = {
        "query": query,
        "start_time": start_date,
        "end_time": end_date,
        "max_results": results_per_request,
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

    final_results = pd.DataFrame(columns = ["text", "created_at", "like_count", "retweet_count", "reply_count", "geo_place_id",
                                            "country_code", "country", "name", "full_name", "bbox"])
    api_requests = 0     # number of requests
    counter = 0   # number of tweets extracted
    json_response = search_twitter(query_params, bearer_token)
    
    if ('data' not in json_response):
        raise RuntimeError("No such data. Invalid query.")

    # sends API requests while more data exists and we haven't got our intended number of tweets
    while (('next_token' in json_response['meta']) and ('data' in json_response) and (counter <= max_tweets)):
        sleep(5)  # added to prevent API from timing out
        api_requests += 1
        json_response = search_twitter(query_params, bearer_token)
        
        # checks if json response returned data, else breaks loop
        if'data' not in json_response:
            break

        # Looks at core data (tweets, like/retweet/reply count, geo_place_id)
        df = pd.DataFrame(json_response["data"])
        df = df.dropna()
        # extracts public metrics from data
        df["retweet_count"] = df["public_metrics"].apply(lambda row: row["retweet_count"])
        df["reply_count"] = df["public_metrics"].apply(lambda row: row["reply_count"])
        df["like_count"] = df["public_metrics"].apply(lambda row: row["like_count"])
        df["geo_place_id"] = df["geo"].apply(lambda row: row["place_id"])
        df = df[["text", "created_at", "like_count", "retweet_count", "reply_count", "geo_place_id"]]
        
        counter += df.shape[0]
        
        # Gets geographic data
        df2 = pd.DataFrame(json_response["includes"]["places"])
        df2 = df2.dropna()
        df2["bbox"] = df2["geo"].apply(lambda row: row["bbox"])
        df2=df2[["id", "country_code", "country", "name", "full_name", "bbox"]]
        df2.columns = ["geo_place_id", "country_code", "country", "name", "full_name", "bbox"]
        
        # Merges geographic data with general tweet data using 'geo_places_id'
        combined = pd.merge(df, df2, how = 'inner', on = 'geo_place_id')
        final_results = pd.concat([final_results, combined], ignore_index= True)
        
        # checks if next token exists (meaning there's more data, else ends loop)
        if ('next_token' not in json_response['meta']):
            break
        
        query_params["next_token"] = json_response["meta"]["next_token"]
    
    # export results to csv
    final_results.to_csv(f'data_output/final_{location}.csv')

    return final_results
    


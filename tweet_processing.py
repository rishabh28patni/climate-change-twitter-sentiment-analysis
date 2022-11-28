#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:59:54 2022

@author: rishabhpatni
"""
import pandas as pd
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #need to do pip install vaderSentiment
import numpy as np
import ast
import os
import re

def clean_tweet(tweet):
  '''
  clean the tweets. Remove profanity, unnecessary characters, spaces, and stopwords.
  '''
  if type(tweet) == float:
      return ""
  r = tweet.lower()

  r = re.sub("'", "", r) # This is to avoid removing contractions in english
  r = re.sub("@[A-Za-z0-9_]+","", r)
  r = re.sub("#[A-Za-z0-9_]+","", r)
  r = re.sub(r'http\S+', '', r)
  r = re.sub('[()!?]', ' ', r)
  r = re.sub('\[.*?\]',' ', r)
  r = re.sub("[^a-z0-9]"," ", r)
  r = r.split()
  stopwords = ["for", "on", "an", "a", "of", "and", "in", "the", "to", "from"]
  r = [w for w in r if not w in stopwords]
  r = " ".join(word for word in r)
  return r


def data_processing():
    '''
    A function that takes in all data files outputted when running queries, and 

    '''
    # find all files that were outputted from twitter API
    list_of_files = [file for file in os.listdir("data_output/") if file.endswith(".csv")]
    
    #loop through files
    for file in list_of_files:
        print(file)
        data = pd.read_csv(f"data_output/{file}", index_col = 0)    
        data["cleaned_tweet"] = data["text"].apply(lambda tweet: clean_tweet(tweet))  #clean tweet
        data = data.drop_duplicates(subset = 'cleaned_tweet', keep = 'first')       # remove duplicates
        data = data.dropna(subset= 'bbox')          # remove all rows with incomplete geographic data
        data["geo_coordinate"]= data["bbox"].apply(lambda tweet:                        # average out bounding box points to get approximate coordinate
                                                   [np.mean(ast.literal_eval(tweet)[0:2:2]),
                                                    np.mean(ast.literal_eval(tweet)[1:3:2])])
        del data["bbox"]
        print("data cleaning done")
        # Apply textblob model
        data["TextBlob_polarity"] = data["cleaned_tweet"].apply(lambda tweet: TextBlob(tweet).polarity)
        data["TextBlob_subjectivity"] = data["cleaned_tweet"].apply(lambda tweet: TextBlob(tweet).subjectivity)
        print("done textblob")
        
        # Apply SentimentIntensityAnalysis model 
        data["nltk_sentiment_category"] = data["cleaned_tweet"].apply(lambda tweet: SentimentIntensityAnalyzer().polarity_scores(tweet))
        data["nltk_sentiment_category"] = data["nltk_sentiment_category"].apply(lambda analysis: "positive" if analysis["compound"] > 0.05 
                                                                                else ("negative" if analysis["compound"] < -0.05 else "neutral"))
        print("model running done")
        
        # Export processed result to csv
        data.to_csv(f"data_output/processed_data_{file.split('_')[-1]}")
    
data_processing()
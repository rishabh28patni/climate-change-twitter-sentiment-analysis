# Sentiment Analysis using Climate Change Twitter Data

## Introduction
This project looks to gather tweet data on climate change using the the Twitter API. After gathering data, data analysis is performed to identify key trends and correlations and give a better understanding of the climate change discourse across twitter. 

There are two parts to running the code on this repository: the data generation and data processing. The data generation requires access to the twitter API and a bearer token that allows you to access the search_tweets_all endpoint (requires academic access). The data processing can be performed if there are output files stored in a subfolder called "/data_output". The data processing involves removing duplicates, getting approximate geo-coordinates of where the tweet was made from, and running two sentiment analysis models and outputting the results in a dataframe. 

## Running Code
To start off, clone the repository locally. Then, in your local terminal, cd your way to the repository and run the following command: 
```
pip install -r requirements.txt
```
This will install all the libraries needed to run the code locally. 

After this, open the main.py file. In the main.py file, you can set the query parameters, start_date, end_date, the max number of tweets you can return, and a location parameter used for naming the downloaded file. Note that this query only generates one file, and you'll need to run multiple queries if you're looking for more information. Also fill out your local bearer token. 

Otherwise, if you're only looking to process the data, set the generate_data parameter to equal False. Then run code. 

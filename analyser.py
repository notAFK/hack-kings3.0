'''This takes all the tweets from a sqlite3 db in their text form and performs
filtering and sentiment analysis on them, returning the features into another
sqlite3 db'''

import sys
import os
from utils import *
import re
import nltk
import requests
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

def init():
    # Download stopwords from nltk
    nltk.download('stopwords')

# Read tweets from db
def read_tweets():
    conn, c = get_database_connection(DATABASES['STUB_RAW_TWEETS_DB'])
    c.execute('''SELECT * FROM ''' + TEST_PARAMS['ANALYSER_COMPANY'] + \
              ''' LIMIT 10000''')
    return conn, c

# Filter a given tweet, removing stopwords and filter weird chars
def filter_tweet(tweet):
    # If it has an URL return none
    r = re.compile(r'(http)|(www)')
    if r.search(tweet):
        return ''
    # Remove stopwords
    if tweet in stopwords.words('english') :
        return ''
    # Remove other characters
    tweet = re.sub(r'^[a-zA-Z0-9 -\'!.;]', '', tweet)
    return tweet

# Return the features of the tweets as a list of tuples
def get_filtered_tweets_features():
    # Get all tweets from db
    conn, c = read_tweets()
    conn.close()
    # Filter them
    features = []
    for tweet in c.fetchall():
        feature = get_sentiment(filter_tweet(tweet[1]))
        features.append((tweet[0], feature))
    return features

# Get the sentiment of a tweet from a json file
def get_sentiment(tweet):
    return vaderSentiment(tweet)

def insert_feature_in_db(feature):

if __name__ == '__main__':
    # Init
    init()
    # Get features from tweets and put them into feature db
    
    for feature in get_filtered_tweets_features():
        insert_feature_in_db(feature)

'''This takes all the tweets from a sqlite3 db in their text form and performs
filtering and sentiment analysis on them, returning the features into another
sqlite3 db'''

import sys
import os
import re
import nltk
import requests
from utils import *
from tqdm import tqdm
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment


def init():
    # Download stopwords from nltk
    nltk.download('stopwords')


# Read tweets from db
def read_tweets(company):
    conn, c = get_database_connection(DATABASES['RAW_TWEETS_DB'])
    c.execute('''SELECT * FROM ''' + company + \
              ''' LIMIT 10000''')
    return conn, c


# Filter a given tweet, removing stopwords and filter weird chars
def filter_tweet(tweet):
    tweet = tweet.decode('utf-8')
    # If it has an URL return none
    r = re.compile(r'(http)|(www)')
    if r.search(tweet):
        return ''
    # Remove stopwords
    if tweet in stopwords.words('english') :
        return ''
    # Remove other characters
    # tweet = re.sub(r'^[a-zA-Z0-9 -\'!.;]', '', tweet)
    return tweet.encode('utf-8')


# Return the features of the tweets as a list of tuples
def get_filtered_tweets_features(company):
    # Get all tweets from db
    conn, c = read_tweets(company)
    # Filter them
    features = []
    for tweet in c.fetchall():
        filtered_tweet = filter_tweet(tweet[1])
        if filtered_tweet == '':
            continue
        feature = get_sentiment(filtered_tweet)
        features.append((tweet[0], feature['neg'], feature['neu'], \
                        feature['pos'], feature['compound']))
    # Close connection
    conn.close()
    return company, features


# Get the sentiment of a tweet from a json file
def get_sentiment(tweet):
    sentiment = vaderSentiment(tweet)
    if VERBOSE:
        print 'Sentiment for ' + tweet + ': ' + str(sentiment)
    return sentiment


def insert_feature_in_db((company, features)):
    conn, c = get_database_connection(DATABASES['FEATURES_DB'])
    c.execute('''CREATE TABLE IF NOT EXISTS ''' + company + \
      ''' (hash INTEGER PRIMARY KEY, neg REAL, neu REAL, pos REAL, com REAL)''')
    for index, feature in tqdm(enumerate(features)):
        c.execute('''INSERT OR IGNORE INTO ''' + company + \
                  ''' VALUES(?, ?, ?, ?, ?)''', \
                  (feature[0], feature[1], feature[2], feature[3], feature[4]))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # TODO: replace test company with real
    company = 'cocacola'
    # Init
    init()
    # Get features from tweets and put them into feature db
    insert_feature_in_db(get_filtered_tweets_features(company))

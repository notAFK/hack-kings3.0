'''This takes all the tweets from a sqlite3 db in their text form and performs
filtering and sentiment analysis on them, returning the features into another
sqlite3 db'''

import sys
import os
import utils
import re
from nltk import stopwords

COMPANY = None

def init(company = None):
    # Download stopwords from nltk
    nltk.download('stopwords')
    # TODO: make this get the company from scraper
    COMPANY = TEST_PARAMS['ANALYSER_COMPANY']

def read_tweets():
    conn, c = get_database_connection(DATABASES['STUB_RAW_TWEETS_DB'])
    c.execute('''SELECT * FROM ? LIMIT 10000''', (COMPANY,))
    return c

def filter_tweet(tweet):
    # If it has an URL return none
    r = re.compile(r'(http)|(www)')
    if r.search(tweet):
        return ''
    # Remove stopwords
    if tweet in stopwords.words('english') :
        return ''
    # Remove other characters
    tweet = re.sub(r'[a-zA-Z0-9 -\']', '', tweet)
    return tweet

def get_filtered_tweets():
    # Get all tweets from db
    c = read_tweets()
    # Filter them
    tweets = []
    for tweet in c.fetchall():
        tweets.append((tweet[0], filter_tweet(tweet[1])))
    return tweets

if __name__ == '__main__':
    # Init
    init()
    # Get filtered tweets
    for tweet in get_filtered_tweets():
        print str(tweet)

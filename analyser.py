'''This takes all the tweets from a sqlite3 db in their text form and performs
filtering and sentiment analysis on them, returning the features into another
sqlite3 db'''

import utils

def init(company = None):
    # TODO: make this get the company from scraper
    COMPANY = TEST_PARAMS['ANALYSER_COMPANY']

def read_tweets():
    conn, c = get_database_connection(DATABASES['STUB_RAW_TWEETS_DB'])
    c.execute('''SELECT * FROM ? LIMIT 10000''', (COMPANY,))
    return c

def filter_tweet(tweet):
    return tweet

def get_filtered_tweets():
    # Get all tweets from db
    c = read_tweets()
    # Filter them
    tweets = []
    for tweet in c.fetchall():
        tweets.append((tweet[0], filter_tweet(tweet[1])))
    return tweets

#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import config
import sqlite3
import os
from tqdm import tqdm
from utils import *

'''
Source of the template along with query operators
http://nocodewebscraping.com/twitter-json-examples/
'''
def init_api():
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    #refer http://docs.tweepy.org/en/v3.2.0/api.html#API
    #tells tweepy.API to automatically wait for rate limits to replenish

    return api


def get_tweets_from_keyword(keyword, max_tweets):
    api = init_api()

    search =tweepy.Cursor(api.search,q=keyword).items()

    tweets = []
    for count in range (1, max_tweets):
        try:
            tweet = next(search)
            #count is the number of tweets
            #use count-break during dev to avoid twitter restrictions
            #10K tweets for training data
        except tweepy.TweepError:
            #catches TweepError when rate limiting occurs, sleeps, then restarts.
            #nominally 15 minnutes, make a bit longer to avoid attention.
            print "sleeping...."
            time.sleep(60*16)
            tweet = next(search)
        except StopIteration:
            break
        try:
            print "Writing to JSON tweet number:"+str(count)
            # json.dump(user._json,file,sort_keys = True,indent = 4)
            # tweets.append(json.loads(tweet))
            tweets.append((tweet._json["id"], tweet._json["text"], \
                            tweet._json["created_at"]))
        except UnicodeEncodeError:
            pass

    return tweets

# Add the tweets in the db
def add_tweets_in_db(tweets, keyword):
    create_tweets_table(DATABASES['RAW_TWEETS_DB'], keyword)
    conn, c = get_database_connection(DATABASES['RAW_TWEETS_DB'])
    # Add the tweets to db
    for index,tweet in tqdm(enumerate(tweets)):
        c.execute('''INSERT OR IGNORE INTO ''' + keyword + \
        ''' VALUES (?,?,?)''' ,(tweet[0], tweet[1], tweet[2]))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    keyword = TEST_PARAMS['ANALYSER_COMPANY']
    max_tweets = TEST_PARAMS['MAX_TWEETS']
    tweets = get_tweets_from_keyword(keyword, max_tweets)
    tweets = tweets + get_tweets_from_keyword('#' + keyword, max_tweets)
    tweets = tweets + get_tweets_from_keyword('@' + keyword, max_tweets)
    add_tweets_in_db(tweets, keyword)

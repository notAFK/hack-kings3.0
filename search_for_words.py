#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import config
import sqlite3
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
            tweets.append(tweet._json["text"])
            
        except UnicodeEncodeError:
            pass
        
    return tweets

    
    #todo: write users to file, search users for interests, locations etc.

if __name__ == "__main__":
    keyword = TEST_PARAMS['ANALYSER_COMPANY']
    max_tweets = TEST_PARAMS['MAX_TWEETS']
    tweets = get_tweets_from_keyword(keyword, max_tweets)

    for tweet in tweets:
        print tweet

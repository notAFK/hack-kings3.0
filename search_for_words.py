#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import config
import sqlite3
import os
import sys
import multiprocessing
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import time
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

def get_tweets_from_keyword_selenium(keyword, max_tweets, tweets_list, kw):
    base_url = URLS['TWITTER_SEARCH_URL']
    browser = webdriver.Chrome()
    url = base_url + keyword

    browser.get(url)
    time.sleep(1)

    body = browser.find_element_by_tag_name('body')

    for _ in range(max_tweets):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    tweets = browser.find_elements_by_class_name('tweet')

    for tweet in tweets:
        if tweet.get_attribute('data-item-id') is None:
            continue
        the_id = tweet.get_attribute('data-item-id')
        the_id = int(the_id)
        text = \
            tweet.find_element_by_class_name('tweet-text').text.encode('utf-8')
        created_at = tweet.find_element_by_class_name('_timestamp')
        created_at = created_at.get_attribute('data-time')
        tweets_list.append((the_id, text, created_at))
    # Add them to db
    add_tweets_in_db(tweets_list, kw)


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
            print "rate error"
            return tweets
        except StopIteration:
            break
        try:
            # print "Writing to JSON tweet number:"+str(count)
            print "Scraping tweet number " + str(count)
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

    keyword = 'microsoft'
    max_tweets = 1000

    if len(sys.argv) == 3:
        keyword = sys.argv[1]
        max_tweets = sys.argv[2]
    tweets = []
    # Number of processes
    jobs = []
    tweets = list()
    # PROC 1
    process = \
        multiprocessing.Process(target=get_tweets_from_keyword_selenium, \
                                args=('%23' + 'surfacebook', max_tweets, tweets, \
                                     keyword))
    jobs.append(process)
    process.start()
    # PROC 2
    process = \
        multiprocessing.Process(target=get_tweets_from_keyword_selenium, \
                                args=('to%3A' + keyword, max_tweets, tweets, \
                                     keyword))
    jobs.append(process)
    process.start()
    # PROC 3
    process = \
        multiprocessing.Process(target=get_tweets_from_keyword_selenium, \
                                args=('surfacepro', max_tweets, tweets, keyword))
    jobs.append(process)
    process.start()
    # Join stuff
    for proc in jobs:
        proc.join()
# =======
    # # keyword = TEST_PARAMS['ANALYSER_COMPANY']
    # # max_tweets = TEST_PARAMS['MAX_TWEETS']
    # # tweets = get_tweets_from_keyword(keyword, max_tweets)

    # # keywords = COMPANIES['Astrazeneca']
    # keywords = "Microsoft"
    # max_tweets = TEST_PARAMS['MAX_TWEETS']

    # tweets = get_tweets_from_keyword(keywords, max_tweets)
    # tweets = tweets + get_tweets_from_keyword('#' + keywords, max_tweets)
    # tweets = tweets + get_tweets_from_keyword('@' + keywords, max_tweets)
    # add_tweets_in_db(tweets, keywords)

    # # The old way to print it out
    # # for keyword in keywords:
        # # tweets = get_tweets_from_keyword(keyword[0], max_tweets)

        # # for tweet in tweets:
            # # print tweet
# >>>>>>> master

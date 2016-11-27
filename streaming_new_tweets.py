#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import config
from utils import *

# This is the listener, resposible for receiving data
class DBListener(tweepy.StreamListener):
    def on_data(self, data):
        # Parsing 
        decoded = json.loads(data)
        # #open a file to store the status objects
        # file = open('streaming_new_tweets.json', 'wb')  
        #write json to file
        json.dump(decoded,file,sort_keys = True,indent = 4)
        #show progress
        print "Writing tweets to file,CTRL+C to terminate the program"

        
        return True

    def on_error(self, status):
        print "Error with status " + status

if __name__ == '__main__':
    l = DBListener()
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)

    #Hashtag to stream
    stream.filter(track=COMPANIES["Microsoft"])  #Replace with your favorite hashtag or query

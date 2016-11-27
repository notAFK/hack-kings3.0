#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import config
from utils import *
from analyser import *
import time

# This is the listener, resposible for receiving data
class DBListener(tweepy.StreamListener):
    def __init__(self ,company_name):
        self.company_name = company_name
        create_tweets_table(DATABASES['RAW_TWEETS_DB'], self.company_name)

    def on_data(self, data):
        # Parsing
        # print data
        decoded = json.loads(data)
        # print "PASSES"
        # file = open('NEW_JSON.json', 'wb')
        # json.dump(decoded,file,sort_keys = True,indent = 4)
    

        if "id" not in decoded:
            print "ID NOT IN DECODED"
            return True
        the_id = decoded['id']
        tweet = decoded['text']
        print tweet
        print "--------------------------------------------------"
        created_at = decoded['created_at']
        created_at = time.mktime(time.strptime(created_at,"%a %b %d %H:%M:%S +0000 %Y"))
        # print created_at
        # #open a file to store the status objects
        #write json to file

        self.write_tweets_to_DB(the_id, tweet, created_at)

        # json.dump(decoded,file,sort_keys = True,indent = 4)
        #show progress
        # print "Writing tweets to file,CTRL+C to terminate the program"


        return True

    def on_error(self, status):
        print "Error with status " + status

    def write_tweets_to_DB(self, the_id, tweet, timestamp):

        self.conn, self.c = get_database_connection(DATABASES['RAW_TWEETS_DB'])
        self.c.execute('''INSERT OR IGNORE INTO ''' + self.company_name + \
                ''' VALUES (?,?,?)''' ,(the_id, tweet, timestamp))

        self.conn.commit()
        self.conn.close()

        self.conn, self.c = get_database_connection(DATABASES['FEATURES_DB'])
        self.c.execute('''CREATE TABLE IF NOT EXISTS ''' + self.company + \
                  ''' (hash INTEGER PRIMARY KEY, value real)''')

        self.c.execute('''INSERT OR IGNORE INTO ''' + self.company + \
                  ''' VALUES(?, ?)''', (feature[0], feature[1]))

        self.conn.commit()
        self.conn.close()


    def get_filtered_tweets_features(self, company):
        # Get all tweets from db
        conn, c = read_tweets(company)
        # Filter them
        features = []
        for tweet in c.fetchall():
            filtered_tweet = filter_tweet(tweet[1])
            if filtered_tweet == '':
                continue
            feature = get_sentiment(filtered_tweet)
            features.append((tweet[0], feature['pos']))
        # Close connection
        conn.close()
        return company, features




if __name__ == '__main__':

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # For more details refer to https://dev.twitter.com/docs/streaming-apis


    company_name = "Microsoft"
    search_query = COMPANIES[company_name]
    # create_tweets_table('FEATURES_DB', company_name )

    l = DBListener(company_name)
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)

    stream = tweepy.Stream(auth, l)

    #Hashtag to stream
    stream.filter(track=[company_name])  #Replace with your favorite hashtag or query

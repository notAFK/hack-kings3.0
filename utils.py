'''Contains general functions used by more than one script. Also contains
global vars'''

import sqlite3
import os

__init__ = ['DATABASES', 'get_database_connection', 'TEST_PARAMS', 'URLS',
            'VERBOSE', 'SENTIMENT_API_KEY', 'create_table']

SENTIMENT_API_KEY = ''
VERBOSE = True
URLS = {'SENTIMENT_API':
    'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'}
TEST_PARAMS = {'ANALYSER_COMPANY': 'starbucks'}
DATABASES = {'RAW_TWEETS_DB': 'raw_tweets.db',
             'FEATURES_DB'  : 'extracted_features.db',
             'STUB_RAW_TWEETS_DB': 'stub_raw_tweets.db'}

def get_database_connection(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    return (conn, c)

def create_table(db_path, table_name):
    conn, c = get_database_connection(db_path)
    c.execute('''CREATE TABLE ''' + table_name + \
              ''' (hash text, tweet text, ts timestamp)''')
    conn.commit()
    conn.close()

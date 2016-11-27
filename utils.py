'''Contains general functions used by more than one script. Also contains
global vars'''

import sqlite3
import os

__init__ = ['DATABASES', 'get_database_connection', 'TEST_PARAMS']

TEST_PARAMS = {'ANALYSER_COMPANY',
               }
DATABASES = {'RAW_TWEETS_DB': 'raw_tweets.db',
             'FEATURES_DB'  : 'extracted_features.db',
             'STUB_RAW_TWEETS_DB': 'stub_raw_tweets.db',
            }

def get_database_connection(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    return (conn, c)

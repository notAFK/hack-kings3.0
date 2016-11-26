'''Contains general functions used by more than one script. Also contains
global vars'''

import sqlite3
import os

__init__ = ['DATABASES', 'get_database_connection']

DATABASES = {'RAW_TWEETS_DB': 'raw_tweets.db',
             'FEATURES_DB'  : 'extracted_features.db'
            }

def get_database_connection(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    return (conn, c)

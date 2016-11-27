'''Contains general functions used by more than one script. Also contains
global vars'''

import sqlite3
import os
import json
import requests

__init__ = ['DATABASES', 'get_database_connection', 'TEST_PARAMS', 'URLS',
            'VERBOSE', 'create_table', 'get_ticker']

URLS = {'COMPANY_NAME_TO_TICKER_API': 'http://chstocksearch.herokuapp.com/api/'}
VERBOSE = True
TEST_PARAMS = {'ANALYSER_COMPANY': 'starbucks OR '
                                    + 'coffee OR '
                                    + 'medusa' ,
                'MAX_TWEETS' : 100 }

COMPANIES = {
        "Apple" : [
            "Apple OR "
            +"#Apple OR "
            +"iPad OR "
            +"iphone OR "
            +"iPod OR "
            +"apple watch OR "
            +"mac OR "
            +"macbook OR "
            +"iMac OR "
            ],
        "Facebook" : [
            "Facebook OR "
            +"#Facebook OR "
            +"news feed OR "
            +"poke OR "
            +"status OR "
            +"timeline OR "
            +"messenger OR "
            ],
        "Costa" : [
            'Costa OR '
            +'#Costa OR '
            +'Whitbread OR '
            ],
        "Microsoft" : [
            'Mircosoft OR '
            +'#Mircosoft OR '
            +'Surface OR '
            +'power point OR '
            +'excel OR '
            +'vista OR '
            +'kinect OR '
            +'bing OR '
            +'visual basic OR '
            +'visual studio OR '
            +'ms-dos OR '
            ],
        "Astrazeneca" : [
            "Astrazeneca OR "
            +"ARIMIDEX OR "
            +"ATACAND OR "
            +"NEXIUM OR "
            +"ONGLYZA OR "
            +"PLENDIL OR "
            +"PRILOSEC OR "
            +"PULMICORT OR "
            +"RHINOCORT OR "
            +"CRESTOR OR "
            +"DALIRESP OR "
            +"SYMBICORT OR "
            +"SYNAGIS OR "
            +"TAGRISSO OR "
            +"FASLODEX OR "
            +"Kombiglyze OR "
            +"Farxiga OR "
            +"Astrazeneca OR "
            +"Astrazeneca OR "
            +"Astrazeneca OR "
            +"Carbocaine  OR "
            +"Citanes OR "
            +"Diprivan OR "
            +"EMLA OR "
            +"MarcaineOR "
            +"Naropin OR "
            +"Xylocaine OR "
            +"Xyloproct OR "
            +"Atacand OR "
            +"Betaloc OR "
            +"BrilintaOR "
            +"Crestor OR "
            +"ExantaOR "
            +"Epanova OR "
            +"Imdur OR "
            +"Inderal OR "
            +"Lexxel OR "
            +"Logimax OR "
            +"Nif-Ten OR "
            +"Plendil OR "
            +"Ramace OR "
            +"SelokenOR "
            +"Tenoretic OR "
            +"Tenormin OR "
            +"Unimax OR "
            +"Zestoretic OR "
            +"Zestril OR "
            +"Bydureon OR "
            +"Byetta OR "
            +"FarxigaOR "
            +"KombiglyzeOR "
            +"Onglyza OR "
            +"Symlin OR "
            +"Xigduo/Xigduo XR OR "
            +"Entocort OR "
            +"LosecOR "
            +"Nexium OR "
            +"Vimovo OR "
            +"ApatefOR "
            +"Avloclor OR "
            +"Cubicin OR "
            +"Foscavir OR "
            +"Lexinor OR "
            +"Merrem/Meronem OR "
            +"Paludrine OR "
            +"SavarineOR "
            +"Synagis OR "
            +"Heminevrin OR "
            +"Mysoline OR "
            +"Seroquel OR "
            +"SeroquelOR "
            +"Vivalan OR "
            +"Zomig OR "
            +"Arimidex OR "
            +"Casodex/Cosudex OR "
            +"Faslodex OR "
            +"Iressa OR "
            +"Lynparza OR "
            +"NolvadexOR "
            +"Tomudex OR "
            +"Zoladex OR "
            +"Caprelsa OR "
            +"Tagrisso OR "
            +"Accolate OR "
            +"Bambec OR "
            +"Bricanyl OR "
            +"Oxis OR "
            +"Pulmicort"
            ]
}

DATABASES = {'RAW_TWEETS_DB': 'raw_tweets.db',
             'FEATURES_DB'  : 'extracted_features.db',
             'STUB_RAW_TWEETS_DB': 'stub_raw_tweets.db'}

def get_database_connection(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    return (conn, c)

def create_tweets_table(db_path, table_name):
    conn, c = get_database_connection(db_path)
    c.execute('''CREATE TABLE ''' + table_name + \
              ''' (hash text, tweet text, ts timestamp)''')
    conn.commit()
    conn.close()

def get_ticker(company):
    response = requests.get(URLS['COMPANY_NAME_TO_TICKER_API'] + company)
    response = json.loads(response.content)
    return (response[0])['symbol']

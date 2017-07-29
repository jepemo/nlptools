# -*- coding: utf-8 -*-
# nlptools - Unix inspired utilities for Natural Language Processing.
#
# Copyright (C) 2017-present Jeremies Pérez Morata
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import json
import re
import TwitterSearch as ts
import sys
import time
from datetime import datetime

def create_parser():
    parser = argparse.ArgumentParser(description='Search tweets with the Twitter API')

    apigroup = parser.add_argument_group(description='API Key Arguments')
    apigroup.add_argument('--consumer_key', help="API Consumer Key", required=True)
    apigroup.add_argument('--consumer_secret', help="API Consumer Secret", required=True)
    apigroup.add_argument('--access_token', help="API Access Token", required=True)
    apigroup.add_argument('--access_token_secret', help="API Token Secret", required=True)

    searchgroup = parser.add_argument_group(description="Search Parameters")
    searchgroup.add_argument("--language", default='en', help="Language of the Tweets")
    searchgroup.add_argument("--latitude", type=str, help="GEO: Latitude")
    searchgroup.add_argument("--longitude", type=str, help="GEO: Longitude")
    searchgroup.add_argument("--count", default=100, type=int, help="Language of the Tweets")
    searchgroup.add_argument("--keywords", nargs='+', type=str, help="Keywords to search")
    searchgroup.add_argument("--enable-entities", action='store_const', const=True, default=False, dest="enable_entities", help="Don't fetch the entities information")

    return parser

it = 1
def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
    global it
    print("IT={0}".format(it), file=sys.stderr)
    it = it+1
    queries, tweets_seen = current_ts_instance.get_statistics()
    if queries > 0 and (queries % 2) == 0: # trigger delay every 5th query
        time.sleep(30) # sleep for 60 seconds

def main(argv=None):
    parser = create_parser()
    args = parser.parse_args(argv)

    api_search = None
    if args.consumer_key and args.consumer_secret and args.access_token and args.access_token_secret:
        api_search = ts.TwitterSearch(
            consumer_key = args.consumer_key,
            consumer_secret = args.consumer_secret,
            access_token = args.access_token,
            access_token_secret = args.access_token_secret
        )
    else:
        api_search = ts.TwitterSearch()

    tso = ts.TwitterSearchOrder()

    if args.language:
        tso.set_language(args.language)

    if args.count:
        tso.set_count(args.count)

    if args.enable_entities:
        tso.set_include_entities(args.enable_entities)

    if args.latitude and args.longitude:
        tso.set_geocode(float(args.latitude), float(args.longitude), 30, imperial_metric=False)
        #print("LON:{0}, LAT:{1}".format(float(args.latitude), float(args.longitude)), file=sys.stderr)

    if args.keywords is None:
        tso.set_keywords(['*'])
    else:
        tso.set_keywords(args.keywords)

    num_tweets = 0
    for tweet in api_search.search_tweets_iterable(tso, callback=my_callback_closure):
        num_tweets = num_tweets + 1

        fecha_parsed = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')
        fecha = fecha_parsed.strftime("%Y%m%d_%H%M%S") #tweet['created_at']
        text = tweet['text'].replace("\n", " ")
        #print( '%s;%s;%s' % ( tweet['user']['screen_name'], fecha, text ) )
        print(text)

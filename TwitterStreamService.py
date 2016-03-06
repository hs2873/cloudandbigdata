
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
from textwrap import TextWrapper
from tweepy import Stream
from elasticsearch import Elasticsearch

consumer_key="kSCEKl0lVyAWRXpNFRNk8VXpL"
consumer_key_secret="zP4DBYsUbwlnTRbtY8wj5cbKCsl7IEXccv74rjZ6I0OPNWQdgM"
access_token="2601074616-d94JMfuZPthDZW4VIUGTCDKXrJFs9SLVwOjIXsn"
access_token_secret="gilQbRAi75s0K0twpQU3w9z9anDhaMySBPz7ej7NkJtRB"
es=Elasticsearch()

class MyStreamListener(StreamListener):
    def on_status(self,status):
        es.create(index='idx_tmp',doc_type='twitter_twp',body=status._json)
        print status._json
        

if __name__=='__main__':
    listener=MyStreamListener()
    auth = OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream=Stream(auth,listener)
    stream.filter(track=['google'])




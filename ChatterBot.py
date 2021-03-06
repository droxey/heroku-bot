# Dependencies
import os
import tweepy
import json
import time

from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY") or os.environ.get(
    "CONSUMER_KEY", "bad")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

print(f'Consumer Key: {consumer_key}')

try:
    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
except Exception, e:
    print(e)


# Create a function that tweets
# CODE GOES HERE

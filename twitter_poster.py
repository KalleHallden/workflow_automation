

import tweepy
from tokens import getCreds

creds = getCreds()

auth = tweepy.OAuthHandler(creds["consumer_key"], creds["consumer_secret"])
auth.set_access_token(creds["access_token"], creds["access_token_secret"])
api = tweepy.API(auth)

tweet_text = "Test"
tweet_image_path = "/photo.png"

status = api.update_with_media(tweet_image_path, tweet_text)
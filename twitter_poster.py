

import tweepy
from tokens import getCreds

def post_to_twitter(image_path, video_title, video_link):
	creds = getCreds()

	auth = tweepy.OAuthHandler(creds["consumer_key"], creds["consumer_secret"])
	auth.set_access_token(creds["access_token"], creds["access_token_secret"])
	api = tweepy.API(auth)

	tweet_text = video_title + " " + video_link

	status = api.update_with_media(image_path, tweet_text)
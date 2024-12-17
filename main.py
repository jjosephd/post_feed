import tweepy
from dotenv import load_dotenv
import os
import feedparser
import pprint

def get_client():
    load_dotenv()

    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )
    return client
def create_tweet(client, tweet_text):
    client.create_tweet(text=tweet_text)
    
#client = get_client()
#create_tweet(client, "Back Again!")

feed = feedparser.parse("https://cointelegraph.com/rss/tag/bitcoin")
pprint.pprint(feed.keys())
    
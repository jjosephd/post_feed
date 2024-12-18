import tweepy
import os
import feedparser
from dotenv import load_dotenv
from article import Article
import pyshorteners

shortener = pyshorteners.Shortener()

def get_client():
    """
    Returns a tweepy.Client for accessing the X API.

    The client is authenticated using credentials from environment variables:
    - CONSUMER_KEY
    - CONSUMER_SECRET
    - ACCESS_TOKEN
    - ACCESS_TOKEN_SECRET

    The environment variables are first loaded from a .env file using the
    python-dotenv library.

    Returns:
        tweepy.Client: authenticated client for accessing the Twitter API
    """
    load_dotenv()

    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )
    return client
def create_tweet(client, article):
    """
    Prints a tweet based on the given Article, then creates a new tweet
    using the Twitter API client.

    The tweet text is constructed by concatenating the article title, link,
    summary, and author. The tweet is then printed to the console, and
    the Twitter API is used to create a new tweet with the same text.

    Args:
        client (tweepy.Client): authenticated client for accessing the Twitter API
        article (Article): the article to be tweeted
    """
    title = article.title
    link = shortener.tinyurl.short(article.link)
    summary = article.summary
    author = article.author
    
    tweet_text = f"Title: {title}\nLink: {link}\nSummary: {summary}\nAuthor: {author}"
    print(tweet_text)
    
    client.create_tweet(text=tweet_text)

    

feed = feedparser.parse("https://www.pff.com/feed/teams/24")
first_article = feed["entries"][0]

article = Article(
    author=first_article["author"],
    link=first_article['link'],
    published=first_article['published'],
    summary=first_article['summary'],
    title=first_article['title']
)
    

client = get_client()
create_tweet(client, article)
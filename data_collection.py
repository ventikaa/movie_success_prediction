import requests
import pandas as pd
import tweepy
from dotenv import load_dotenv
import os
from src.sentiment_analysis import analyze_sentiment

load_dotenv()  # Load API keys from .env file

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")

def fetch_tmdb_data(movie_ids):
    movies_data = []
    for movie_id in movie_ids:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            movies_data.append(response.json())
    return pd.DataFrame(movies_data)

def fetch_twitter_sentiment(movie_titles):
    auth = tweepy.AppAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    api = tweepy.API(auth)
    sentiment_data = []
    for title in movie_titles:
        tweets = api.search(q=title, lang='en', count=100)
        sentiment_score = analyze_sentiment(tweets)
        sentiment_data.append({'title': title, 'sentiment': sentiment_score})
    return pd.DataFrame(sentiment_data)

if __name__ == "__main__":
    movie_ids = [550, 24428]  # Example movie IDs
    movies_df = fetch_tmdb_data(movie_ids)
    sentiment_df = fetch_twitter_sentiment(["Inception", "The Avengers"])
    movies_df.to_csv('../data/movies.csv', index=False)
    sentiment_df.to_csv('../data/social_media.csv', index=False)

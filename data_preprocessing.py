import pandas as pd

def preprocess_movie_data(movie_df):
    movie_df.dropna(subset=['budget', 'revenue'], inplace=True)
    movie_df['release_date'] = pd.to_datetime(movie_df['release_date'])
    return movie_df

def preprocess_sentiment_data(sentiment_df):
    sentiment_df['sentiment'] = sentiment_df['sentiment'].astype(float)
    return sentiment_df

if __name__ == "__main__":
    movies_df = pd.read_csv('../data/movies.csv')
    sentiment_df = pd.read_csv('../data/social_media.csv')
    movies_df = preprocess_movie_data(movies_df)
    sentiment_df = preprocess_sentiment_data(sentiment_df)
    movies_df.to_csv('../data/movies_cleaned.csv', index=False)
    sentiment_df.to_csv('../data/sentiment_cleaned.csv', index=False)

import src.data_collection as dc
import src.data_preprocessing as dp
import src.feature_engineering as fe
import src.model_training as mt

if __name__ == "__main__":
    movie_ids = [550, 24428]
    movies_df = dc.fetch_tmdb_data(movie_ids)
    sentiment_df = dc.fetch_twitter_sentiment(["Inception", "The Avengers"])
    
    movies_df.to_csv('data/movies.csv', index=False)
    sentiment_df.to_csv('data/social_media.csv', index=False)

    movies_df = dp.preprocess_movie_data(movies_df)
    sentiment_df = dp.preprocess_sentiment_data(sentiment_df)

    movies_df = fe.add_cast_popularity_feature(movies_df)
    movies_df = fe.add_genre_feature(movies_df)

    model = mt.train_model(movies_df)

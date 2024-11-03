import pandas as pd

def add_cast_popularity_feature(movie_df):
    movie_df['cast_popularity'] = movie_df['cast'].apply(lambda x: sum([actor['popularity'] for actor in x]) / len(x))
    return movie_df

def add_genre_feature(movie_df):
    movie_df['is_action'] = movie_df['genres'].apply(lambda x: 1 if 'Action' in x else 0)
    return movie_df

if __name__ == "__main__":
    movies_df = pd.read_csv('../data/movies_cleaned.csv')
    movies_df = add_cast_popularity_feature(movies_df)
    movies_df = add_genre_feature(movies_df)
    movies_df.to_csv('../data/movies_featured.csv', index=False)

# Movie Success Prediction Using Multi-Source Data

## Overview
This project aims to predict the success of movies at the box office based on a combination of features like cast popularity, genre, budget, social media sentiment, and release timing. By integrating data from multiple sources (such as TMDb, social media, and historical box office data), this model leverages a variety of factors to provide a robust prediction of movie success.

### Features
- Multi-source data integration: Combines data from APIs and datasets (e.g., TMDb API, social media, historical box office).
- Natural Language Processing (NLP): Analyzes social media sentiment to gauge public opinion on movies.
- Feature Engineering: Constructs relevant features for prediction, including cast popularity, genre impact, budget, and release timing.
- Predictive Modeling: Uses regression models to predict box office success.

## Setup and Installation

### Prerequisites

Ensure you have Python 3.7+ installed. This project also requires the TMDb API and Twitter API (or other social media APIs) keys.

1. Clone the repository:
    git clone https://github.com/yourusername/movie-success-prediction.git
    cd movie-success-prediction
    ```

2. Install dependencies:
    pip install -r requirements.txt
    ```

3. API Keys:
    - TMDb API Key: Sign up on [TMDb](https://www.themoviedb.org/) and get an API key.
    - Twitter API Key: Sign up on [Twitter Developer](https://developer.twitter.com/) and get an API key (optional, for social media sentiment analysis).
    - Add these keys to an `.env` file or directly to the `data_collection.py` and `sentiment_analysis.py` scripts.

### Required Datasets

- `movies.csv` and `box_office.csv`: Obtain historical box office data from sources like [Box Office Mojo](https://www.boxofficemojo.com/) or [Kaggle](https://www.kaggle.com/).
- `social_media_sentiment.csv`: This file is created during the sentiment analysis step.

## Usage

### Data Collection

Run the `data_collection.py` script to fetch movie details, cast information, and other features from TMDb API:
python scripts/data_collection.py
```

### Sentiment Analysis

Use `sentiment_analysis.py` to analyze social media sentiment related to movies:

```bash
python scripts/sentiment_analysis.py
```

### Feature Engineering

Generate additional features for the model (e.g., release timing, genre popularity):

```bash
python scripts/feature_engineering.py
```

### Model Training and Evaluation

Train the regression model to predict box office performance:

```bash
python scripts/model_training.py
```

## Project Walkthrough

### 1. Data Collection

Using `data_collection.py`, we gather data from TMDb and other sources, saving it to `movies.csv` and `box_office.csv`. This data provides foundational information on movie budget, genres, and cast.

### 2. Sentiment Analysis

The `sentiment_analysis.py` script utilizes Twitter data to gauge audience sentiment before release. The script cleans and analyzes the text to create a sentiment score, which is saved in `social_media_sentiment.csv`.

### 3. Feature Engineering

In `feature_engineering.py`, additional features are created:
- **Cast Popularity**: Average popularity of cast members.
- **Genre**: Impact of specific genres.
- **Timing**: Influence of release dates.

### 4. Model Training

Finally, `model_training.py` builds a regression model to predict box office performance. After training, the model outputs evaluation metrics like the R-squared score, showing how well the model predicts movie success.

## Example Results

The output of the model might look like:
- **Average R-squared score**: 0.72 (varies depending on data and model)
- **Feature Importance**: Insights on factors like cast popularity or social media sentiment.

## Dependencies

Listed in `requirements.txt`:
- `textblob` for sentiment analysis
- `pandas`, `numpy` for data processing
- `scikit-learn` for machine learning
- `tweepy` for Twitter API integration

## Future Improvements

- **Incorporate additional social media platforms**: Expand sentiment analysis to other platforms like Instagram and Reddit.
- **Add ensemble models**: Improve accuracy by integrating multiple models.
- **Enhance feature set**: Use additional factors, like promotional budget and award nominations.

## License

This project is licensed under the MIT License.

---

Feel free to reach out with questions or contributions!

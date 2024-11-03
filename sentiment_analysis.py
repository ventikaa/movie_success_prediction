from textblob import TextBlob
import re

def clean_tweet(tweet):
    """
    Clean tweet text by removing links, special characters, and unnecessary whitespace.
    """
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'\@\w+|\#', '', tweet)  # Remove @mentions and hashtags
    tweet = re.sub(r'\W', ' ', tweet)  # Remove non-alphanumeric characters
    return tweet.strip()

def analyze_sentiment(tweets):
    """
    Analyze the sentiment of a list of tweets and return an average sentiment score.
    
    Parameters:
    - tweets (list): List of tweet objects (from Tweepy) or raw tweet texts.

    Returns:
    - float: Average sentiment score across all tweets (between -1 and 1, where
             negative values indicate negative sentiment, and positive values indicate positive sentiment).
    """
    total_sentiment = 0
    count = 0

    for tweet in tweets:
        try:
            # Clean tweet text for more accurate sentiment analysis
            text = clean_tweet(tweet.text if hasattr(tweet, 'text') else tweet)
            
            # Analyze sentiment using TextBlob
            analysis = TextBlob(text)
            sentiment_score = analysis.sentiment.polarity
            
            # Filter out neutral tweets to focus on polarized sentiment
            if sentiment_score != 0:
                total_sentiment += sentiment_score
                count += 1
        except Exception as e:
            print(f"Error analyzing tweet sentiment: {e}")
            continue
    
    # Avoid division by zero in case of no valid sentiment scores
    average_sentiment = total_sentiment / count if count > 0 else 0
    return average_sentiment

if __name__ == "__main__":
    # Example usage
    sample_tweets = [
        "Absolutely loved this movie! A masterpiece!",
        "The plot was all over the place. Not a fan.",
        "Amazing visuals and storyline. Highly recommend!",
        "Boring and predictable. I almost fell asleep.",
        "An unforgettable experience! Will watch again.",
        "Not worth the hype. I expected more.",
        "Outstanding performance by the lead actor!",
        "The movie was okay. Not bad, but not great either.",
        "Beautiful cinematography, but the story lacked depth.",
        "I loved every single moment of it!",
        "The pacing was slow, and it dragged on for too long.",
        "A must-watch! One of the best movies this year.",
        "The jokes didn't land. Could've been funnier.",
        "Felt like a waste of time. Disappointing.",
        "This film was a breath of fresh air. Truly enjoyable.",
        "The plot twist was amazing! Didn't see that coming.",
        "Overrated. I wouldn’t watch it again.",
        "It was good but nothing extraordinary.",
        "One of the worst movies I've seen recently.",
        "Mind-blowing! The director outdid themselves.",
        "The acting was mediocre, to be honest.",
        "Brilliant soundtrack! Fits perfectly with the scenes.",
        "It's just okay. I've seen better.",
        "Fantastic storyline and great direction!",
        "Nothing new here. Pretty standard stuff.",
        "Such an emotional rollercoaster. I cried!",
        "Predictable ending, but still a decent watch.",
        "Highly overrated. Didn't live up to expectations.",
        "A solid film with a powerful message.",
        "Not my type of movie, but it was well made.",
        "Top-notch acting and great chemistry between the leads.",
        "The script was weak and filled with clichés.",
        "Loved the soundtrack and visuals!",
        "Could've been much better. Disappointing.",
        "A fantastic journey from start to finish!",
        "Just an average movie. Nothing special.",
        "The plot development was weak.",
        "Purely magical! Captivating from the first scene.",
        "The characters were bland and forgettable.",
        "One of my favorite movies of all time!",
        "I found it hard to follow the storyline.",
        "A beautiful blend of emotion and adventure!",
        "So boring, I almost walked out halfway.",
        "Perfect for fans of the genre. Very well made.",
        "Decent movie, but not as good as expected.",
        "Brilliantly executed! Deserves all the awards.",
        "Not for everyone, but I personally loved it.",
        "Had potential, but didn’t quite hit the mark.",
        "Exceptional cinematography! Stunning shots.",
        "The movie was just plain awful.",
        "Highly entertaining! I’d definitely recommend it."
    ]
    
    # Run sentiment analysis on sample tweets
    avg_sentiment = analyze_sentiment(sample_tweets)
    print(f"Average Sentiment Score: {avg_sentiment:.2f}")

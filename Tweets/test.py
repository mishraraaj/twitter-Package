import src
import pandas as pd


def test_Clean_text():
    test_df = pd.read_csv("Tweets.csv")
    test_df = src.tweet_sentiments()
    test_df['text'] = test_df['text'].apply(test_df.cleaning_text)
    assert test_df['text']

print(test_Clean_text())
import pandas as pd
import re

tw_df = pd.read_csv("D:/projects/twtr/Tweets/Tweets.csv")

tw_df = tw_df.rename(columns={'airline_sentiment': 'Sentiment',
    'airline_sentiment_confidence': 'confidence'})
tw_df['Sentiment'].replace({'positive':'0','negative':'1'},inphase=True)

tw_df=tw_df[tw_df['Sentiment']!='neutral']


def remove_URL(sample):
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", sample)
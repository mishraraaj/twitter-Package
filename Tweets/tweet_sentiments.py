import pandas as pd
import re

tw_df = pd.read_csv("D:/projects/twttr/Tweets/Tweets.csv")


tw_df = tw_df.rename(columns={'airline_sentiment': 'Sentiment',
    'airline_sentiment_confidence': 'confidence'})

tw_df['Sentiment'].replace({'positive':'0','negative':'1'})

tw_df=tw_df[tw_df['Sentiment']!='neutral']


import re
def cleaning_text(sample):
    """Remove URLs from a sample string"""
    sample=re.sub(r"http\S+", "", sample)
    sample=re.sub(r'@\w+ ?', '',sample )
    sample=re.sub(r'# \w+ ?', '',sample )
    return sample

tw_df['text']=tw_df['text'].apply(cleaning_text)

#remove puncuations
tw_df['text']=tw_df['text'].str.replace('[^\w\s]','')

print(tw_df.info())
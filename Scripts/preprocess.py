"""
preprocess.py
-------------
Standalone preprocessing script for the Reddit Mental Health Corpus.
Produces a cleaned CSV ready for main_notebook.ipynb.

Usage:
    python scripts/preprocess.py --input data/mental-health-data.csv \
                                  --output data/mental-health-clean.csv
"""

import argparse
import re
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

for resource in ['punkt', 'stopwords', 'wordnet', 'punkt_tab']:
    nltk.download(resource, quiet=True)

MH_SUBS = {
    'anxiety', 'ptsd', 'stress', 'domesticviolence', 'survivorsofabuse'
}
CTRL_SUBS = {
    'relationships', 'assistance', 'homeless', 'almosthomeless', 'food_pantry'
}

_lemm = WordNetLemmatizer()
_stop = set(stopwords.words('english'))


def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[@#]\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in _stop and len(t) > 2]
    return ' '.join([_lemm.lemmatize(t) for t in tokens])


def clean(df):
    # Drop missing
    df = df.dropna(subset=['text', 'subreddit'])

    # Remove duplicates
    df = df.drop_duplicates(subset=['text'], keep='first')

    # Standardize subreddit
    df['subreddit'] = df['subreddit'].str.lower().str.strip()

    # Category labels
    df['category'] = df['subreddit'].apply(
        lambda x: 'mental_health' if x in MH_SUBS
        else ('control' if x in CTRL_SUBS else 'other')
    )
    df = df[df['category'] != 'other'].copy()
    df['is_mh'] = (df['category'] == 'mental_health').astype(int)

    # Numeric columns
    for col in ['score', 'num_comments']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col].fillna(df[col].median(), inplace=True)

    # Timestamp features
    if 'social_timestamp' in df.columns:
        df['social_timestamp'] = pd.to_datetime(
            df['social_timestamp'], unit='s', errors='coerce'
        )
        df['hour']        = df['social_timestamp'].dt.hour.fillna(0).astype(int)
        df['day_of_week'] = df['social_timestamp'].dt.dayofweek.fillna(0).astype(int)
        df['month']       = df['social_timestamp'].dt.month.fillna(0).astype(int)
        df['is_weekend']  = df['day_of_week'].isin([5, 6]).astype(int)

    # Derived text features
    df['word_count']    = df['text'].apply(lambda t: len(str(t).split()))
    df['post_length']   = df['text'].apply(lambda t: len(str(t)))
    df['text_clean']    = df['text'].apply(preprocess_text)
    df['engagement_rate'] = df['num_comments'] / (df['score'] + 1) \
                            if 'num_comments' in df.columns else 0

    return df.reset_index(drop=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',  default='data/mental-health-data.csv')
    parser.add_argument('--output', default='data/mental-health-clean.csv')
    args = parser.parse_args()

    print(f"Loading {args.input}...")
    raw = pd.read_csv(args.input, low_memory=False, on_bad_lines='skip')
    print(f"Raw shape: {raw.shape}")

    cleaned = clean(raw)
    print(f"Cleaned shape: {cleaned.shape}")

    cleaned.to_csv(args.output, index=False)
    print(f"Saved to {args.output}")
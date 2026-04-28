"""
augment.py
----------
Corpus augmentation using WordNet synonym substitution (EDA technique).
Balances mental_health and control classes to TARGET_PER_CLASS each.

Usage:
    python scripts/augment.py --input data/mental-health-clean.csv \
                               --output data/mental-health-augmented.csv
"""

import argparse
import random
import pandas as pd
from nltk.corpus import stopwords, wordnet
import nltk

for resource in ['stopwords', 'wordnet', 'omw-1.4']:
    nltk.download(resource, quiet=True)

TARGET_PER_CLASS = 6_000
_STOP_AUG = set(stopwords.words('english'))


def synonym_replace(text, n=3, seed=42):
    random.seed(seed)
    words = str(text).split()
    if len(words) < 5:
        return text
    idxs = [i for i, w in enumerate(words)
             if w.lower() not in _STOP_AUG and w.isalpha() and len(w) > 3]
    random.shuffle(idxs)
    out = words[:]
    replaced = 0
    for i in idxs:
        syns   = wordnet.synsets(words[i])
        lemmas = [l.name().replace('_', ' ')
                  for s in syns for l in s.lemmas()
                  if l.name().lower() != words[i].lower()]
        if lemmas:
            out[i] = random.choice(lemmas)
            replaced += 1
        if replaced >= n:
            break
    return ' '.join(out)


def augment_class(source_df, n_needed, base_seed=0):
    pool = source_df.reset_index(drop=True)
    rows = []
    for j in range(n_needed):
        src_row  = pool.iloc[j % len(pool)].to_dict()
        n_sub    = [2, 3, 5][j % 3]
        aug_text = synonym_replace(src_row['text'], n=n_sub, seed=base_seed + j)
        src_row.update({
            'text':         aug_text,
            'word_count':   len(aug_text.split()),
            'post_length':  len(aug_text),
            'is_augmented': 1
        })
        rows.append(src_row)
    return pd.DataFrame(rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',  default='data/mental-health-clean.csv')
    parser.add_argument('--output', default='data/mental-health-augmented.csv')
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df['is_augmented'] = 0

    n_mh   = (df['category'] == 'mental_health').sum()
    n_ctrl = (df['category'] == 'control').sum()
    need_mh   = max(0, TARGET_PER_CLASS - n_mh)
    need_ctrl = max(0, TARGET_PER_CLASS - n_ctrl)

    print(f"Augmenting: MH needs {need_mh}, Control needs {need_ctrl}")

    aug_mh           = augment_class(df[df['category']=='mental_health'], need_mh,   1000)
    aug_ctrl         = augment_class(df[df['category']=='control'],       need_ctrl, 2000)
    aug_mh['category']   = 'mental_health'
    aug_ctrl['category'] = 'control'

    out = pd.concat([df, aug_mh, aug_ctrl], ignore_index=True)
    out.to_csv(args.output, index=False)
    print(f"Saved {len(out):,} rows to {args.output}")
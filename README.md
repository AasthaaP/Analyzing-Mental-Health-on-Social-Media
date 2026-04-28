
# Analyzing Mental Health on Social Media
## Exploring Linguistic Patterns, Network Dynamics, and Crisis Detection in Online Mental Health Communities
### CSCE 676 Data Mining and Analysis - Texas A&M University

---

> **Start here:** [`main_notebook.ipynb`](./main_notebook.ipynb)

> **Project Video:** [Watch here](https://youtu.be/DmndeI9yIbQ)

---

## Overview

Every day, thousands of people turn to Reddit to talk about their mental health. They write
about panic attacks at 2 AM, about finally leaving abusive relationships, about not being able
to get out of bed. These posts are raw, honest, and detailed in a way that clinical datasets
rarely are.

This project takes those posts seriously as data. Using the Reddit Mental Health Corpus, we
apply a layered suite of data mining techniques to answer a deceptively simple question: **can
we find structure in how people talk about mental health online, and does that structure tell us
something meaningful?**

The answer, it turns out, is yes, on three distinct fronts. Word co-occurrence patterns in
mental health posts are tighter and more clinically specific than in control posts. Segmenting
the corpus by community type surfaces rule sets that a global model completely averages away.
And when you treat a user's post history as a sequence, vocabulary persistence emerges as a
dominant behavioral pattern that unordered mining cannot see at all.

The methods used span classical frequent itemset mining (Apriori, FP-Growth), conditioned
pattern analysis, and sequential pattern mining (PrefixSpan), all applied to a real,
messy, human dataset with the care that subject matter demands.

---

## Research Questions

| # | Question | Method |
|---|----------|--------|
| RQ1 | What frequent word co-occurrence patterns emerge in mental health vs. control posts, and how do confidence and lift compare across varying support thresholds? | Apriori, FP-Growth |
| RQ2 | How do frequent co-occurrence patterns differ between behavioral segments, mental health vs. control users, and daytime vs. late-night posters? | Conditioned FP-Growth |
| RQ3 | Does ordering posts chronologically per user reveal sequential vocabulary dependencies that unordered itemset mining cannot detect? | PrefixSpan |

### Why these three questions?

RQ1 establishes the baseline: do mental health posts have a different co-occurrence fingerprint
than control posts? RQ2 goes deeper by asking whether that fingerprint changes depending on
*who* is posting and *when*. RQ3 changes the frame entirely, instead of looking at individual
posts, it asks whether a user's posting *history* carries sequential structure. Together they
move from vocabulary to community to individual behavior, building a progressively richer
picture of mental health discourse.

---

## Results Summary

**RQ1:** The strongest association rule in mental health posts is `panic -> attack` with a lift
of 22.5. This means the two words co-occur 22 times more often than chance would predict —
confirming that clinical compound phrases are a reliable fingerprint of mental health discourse.
The equivalent top rule in control posts is `bill -> pay` (lift 8.4), reflecting practical
resource-seeking language. The two rule sets are semantically non-overlapping.

**RQ2:** Category-conditioned FP-Growth surfaces 79 to 88 patterns that are completely
invisible in a global model. Segmenting by community type is far more informative than
segmenting by time of day, even though mental health posts peak significantly later in the
evening (hour 20 UTC vs. hour 17 for control posts). The implication is that *what* people say
is a stronger signal than *when* they say it.

**RQ3:** PrefixSpan reveals that vocabulary persistence is the dominant sequential pattern.
Users who post about `feel` tend to post about `feel` again. This structural finding is invisible
to FP-Growth and suggests that stable, recurring emotional themes define individual posting
behavior over time, which has real implications for longitudinal crisis detection.

---

## Dataset

**Name:** Reddit Mental Health Corpus  
**Source:** https://www.kaggle.com/datasets/ruchi798/stress-analysis-in-social-media  
**File:** `mental-health-data.csv`  
**Size:** 4,081 posts, 116 columns  
**Format:** CSV with raw post text, pre-computed LIWC linguistic features, and engagement metrics

### Subreddit breakdown

| Category | Subreddits | Why included |
|----------|-----------|--------------|
| Mental Health | anxiety, ptsd, stress, domesticviolence, survivorsofabuse | Clinically defined distress communities |
| Control | relationships, assistance, homeless, almosthomeless, food_pantry | Emotionally weighted but not clinical |

The control subreddits were chosen carefully. They cover topics that share emotional weight
with mental health communities — relationship difficulty, financial hardship, housing
instability, without being clinically defined mental health spaces. This reduces the risk that
any differences we find are simply due to topic domain rather than mental health status.

### Why this dataset over the alternatives

Three candidate datasets were evaluated before selecting this one:

- **Twitter Mental Health Dataset:** Rejected. The 280-character limit severely restricts text
  richness, and high bot presence contaminates linguistic signals.
- **CounselChat Q&A Dataset:** Rejected. High quality but only 2,000 entries with no temporal
  or network dimensions, making RQ2 and RQ3 impossible.
- **Reddit Mental Health Corpus (selected):** Long-form text, timestamps, engagement metrics,
  and community structure. Uniquely supports all three research questions.

### Accessing the data

The dataset is not committed to this repo due to file size. To reproduce the full analysis:

1. Download `mental-health-data.csv` from the Kaggle link above
2. Upload it to your Google Drive at: `MyDrive/Data_Mining/mental-health-data.csv`
3. The notebook mounts Drive and loads from this path automatically

See [`data/README.md`](./data/README.md) for full preprocessing documentation including every
cleaning decision, the reasoning behind it, and validation tests confirming each step.

---

## Methodology at a Glance

### Data pipeline

```text
Raw CSV (4,081 posts, 116 cols)
|
v
Cleaning & Validation          Section 4
(missing values, duplicates,
timestamps, category labels)
|
v
Exploratory Data Analysis      Section 5
(univariate, bivariate,
text, temporal, network)
|
v
Corpus Augmentation            Section 6
(WordNet synonym substitution,
balanced to 6,000 per class)
|
v
Transaction Construction       Section 7
(top-200 chi-squared tokens,
binary encoding)
|
v
RQ1: Apriori + FP-Growth       Section 8
RQ2: Conditioned FP-Growth     Section 9
RQ3: PrefixSpan                Section 10
|
v
Synthesis + Limitations        Sections 11-12
```

### Key design decisions

**Vocabulary selection:** Instead of using all words, the top 200 tokens by chi-squared
statistic were selected. This keeps the transaction matrix tractable while ensuring the
vocabulary is maximally discriminative between categories.

**Support threshold:** A sweep from 0.001 to 0.10 was run before selecting min_support = 0.01.
This produces roughly 200 itemsets in under 5 seconds, dense enough for meaningful rules,
sparse enough for interpretable output.

**Corpus augmentation:** WordNet synonym substitution (the EDA technique from Wei and Zou,
2019) was used to balance classes to 6,000 posts each. Augmented posts are flagged with
`is_augmented = 1` throughout all analyses for full transparency.

---

## How to Reproduce

This project was built entirely in **Google Colab** with **Python 3.12.13**.

1. Clone or download this repo
2. Upload `mental-health-data.csv` to Google Drive at `MyDrive/Data_Mining/mental-health-data.csv`
3. Open `main_notebook.ipynb` in Google Colab
4. Go to Runtime → Run all
5. All dependencies install automatically in the first cell

If you want to run the preprocessing and augmentation steps as standalone scripts outside
of Colab, use the scripts in `scripts/`:

```bash
python scripts/preprocess.py --input data/mental-health-data.csv \
                              --output data/mental-health-clean.csv

python scripts/augment.py --input data/mental-health-clean.csv \
                           --output data/mental-health-augmented.csv
```

Full dependency list: [`requirements.txt`](./requirements.txt)

---

## Key Dependencies

| Package | Version | Used for |
|---------|---------|---------|
| Python | 3.12.13 | Runtime |
| pandas | 2.x | Data manipulation |
| numpy | 1.x | Numerical operations |
| scikit-learn | 1.4+ | TF-IDF, chi-squared feature selection |
| mlxtend | 0.23+ | Apriori, FP-Growth, association rules |
| prefixspan | latest | Sequential pattern mining |
| nltk | 3.8+ | Tokenization, lemmatization, stopwords |
| networkx | 3.x | User-subreddit graph analysis |
| matplotlib | 3.x | All visualizations |
| seaborn | 0.13+ | Statistical plots |
| textblob | 0.18+ | Sentiment polarity and subjectivity |
| scipy | 1.11+ | Mann-Whitney U, chi-square tests |

---

## Repo Structure

```text
Analyzing-Mental-Health-on-Social-Media/
│
├── main_notebook.ipynb            <- Main deliverable: full analysis, start here
├── requirements.txt               <- Full Colab environment snapshot
├── README.md                      <- You are here
├── .gitignore
│
├── checkpoints/
│   ├── checkpoint_1.ipynb         <- Checkpoint 1: dataset selection and initial EDA
│   └── checkpoint_2.ipynb         <- Checkpoint 2: preprocessing and RQ development
│
├── scripts/
│   ├── preprocess.py              <- Cleans raw CSV and extracts features
│   └── augment.py                 <- Balances classes via synonym substitution
│
├── assets/
│   └── 337002019_DMA_Project_PPT.pptx  <- Project slide deck
│
└── data/
    └── README.md                  <- Dataset source, download instructions, preprocessing notes
```

---

## Potential Applications

This work is exploratory and academic, but the patterns it surfaces point toward several
real-world directions:

**Crisis detection:** The vocabulary persistence finding from RQ3 suggests that longitudinal
monitoring of a user's token distribution could flag escalation from general emotional language
toward clinical crisis language. This is fundamentally different from single-post classifiers
and could reduce false positives significantly.

**Content moderation:** Category-conditioned rule sets from RQ2 could seed keyword lists for
automated flagging systems, not as a replacement for human moderators, but as a first-pass
triage layer that surfaces posts warranting closer attention.

**Platform design:** The late-night posting peak in mental health communities (hour 20 UTC)
suggests that moderation coverage and automated resource-surfacing should be prioritized during
evening hours rather than distributed uniformly across the day.

**Mental health research:** The cross-posting patterns identified in network analysis show that
users in mental health communities frequently also post in economic hardship subreddits. This
co-occurrence of psychological and material distress is a finding that clinical researchers
could pursue with richer data.

**Public health surveillance:** At scale, the linguistic fingerprints identified here could
contribute to population-level mental health monitoring, tracking whether crisis-related
vocabulary is increasing or shifting across communities over time.

---

## Ethical Considerations

Working with mental health data carries responsibilities that go beyond technical correctness.

All data used in this project is publicly available under Reddit's terms of service. No
personally identifiable information is stored, analyzed, or published anywhere in this repo.
User IDs used in the network and sequential analyses are synthetic, derived from post IDs.

The patterns identified here are population-level statistical findings. They are not tools for
identifying specific individuals in crisis, and this project makes no claim that they could or
should be used that way. The goal is to understand community-level structure, not to surveil
individuals.

Subreddit membership is used as a community-level label, not as a proxy for individual
clinical diagnosis. Posting in r/anxiety does not confirm that a person has an anxiety
disorder. All category labels in this project are approximations at the community level.

---

## Author

**Aastha Patel** | UIN: 337002019  
CSCE 676 Data Mining and Analysis  
Texas A&M University

---

## Acknowledgments

- Reddit Mental Health Corpus dataset providers on Kaggle
- PushShift Reddit API for historical data access
- mlxtend and prefixspan open-source maintainers
- Wei and Zou (2019) for the EDA augmentation technique


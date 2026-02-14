# Reddit Mental Health & Community Analysis
## A Data Mining Project Exploring Linguistic Patterns, Network Dynamics, and Crisis Detection in Online Mental Health Communities

---

## Project Overview

This project analyzes mental health discourse on Reddit to uncover linguistic patterns, community dynamics, and crisis signals in online mental health communities. By combining traditional data mining techniques (text mining, clustering, graph analysis) with modern transformer-based approaches (BERT embeddings, topic modeling), we aim to answer questions like:

- **Can linguistic features effectively distinguish mental health posts from control posts?**
- **What network structures emerge from user interactions across mental health subreddits?**
- **Do temporal patterns reveal crisis-driven vs. situational posting behaviors?**
- **Can we predict post engagement based on linguistic and temporal features?**

---

## Dataset

**Source:** Kaggle / Reddit Mental Health Corpus  
**Primary Links:**
- [Stress Analysis in Social Media](https://www.kaggle.com/datasets/ruchi798/stress-analysis-in-social-media)
- [Sentiment Analysis for Mental Health](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health)

**Size:** ~10,000 posts across multiple subreddits  
**Structure:** CSV/JSON format with post content, metadata, and user information

### Key Characteristics:
- **Text Data:** Post titles and body content from mental health and control subreddits
- **Categorical:** Subreddit names (depression, anxiety, ptsd, suicidewatch, relationships, etc.)
- **Numerical:** Engagement metrics (upvotes, comments), post length, word count
- **Temporal:** Timestamps (UTC), day of week, hour of day
- **Network:** User interactions, reply chains, cross-posting patterns

---

## Primary Research Directions

1. **Classification Models:** Build interpretable models distinguishing mental health from control posts using linguistic, temporal, and network features
2. **Network Analysis:** Apply centrality measures and community detection to understand the support-seeking ecosystem
3. **Feature Engineering:** Identify optimal feature combinations balancing predictive accuracy and interpretability
4. **Engagement Modeling:** Investigate factors driving post visibility and community response patterns

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/AasthaaP/Analyzing-Mental-Health-on-Social-Media.git
cd Analyzing-Mental-Health-on-Social-Media
```

### 2. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn
pip install nltk spacy wordcloud textblob
pip install networkx python-louvain
pip install transformers torch
pip install scipy statsmodels
python -m spacy download en_core_web_sm
```

### 3. Download the Dataset
- Download from [Kaggle](https://www.kaggle.com/datasets/ruchi798/stress-analysis-in-social-media)

### 4. Run the Notebook
```bash
jupyter notebook 337002019_CheckPoint1.ipynb
```

---

## Potential Applications

- **Crisis Detection Systems:** Early warning systems for mental health platforms
- **Community Moderation:** Identifying posts requiring professional intervention
- **Mental Health Research:** Understanding linguistic markers of different conditions
- **Platform Design:** Informing supportive features in social media applications
- **Public Health:** Population-level mental health trend monitoring


---

**Author:** Aastha Patel  
**UIN:** 337002019  
**Course:** Data Mining Project at Texas A&M University  

---

## Acknowledgments

- Dataset providers on Kaggle
- Reddit API (PushShift) for historical data access

---

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

## Key Insights

From our Exploratory Data Analysis CheckPoint 1, we have identified five core observations:

### 1. **Linguistic Divergence Between Groups**
**Observation:** Mental health posts emphasize emotional vocabulary ("feel", "anxiety", "day") while control posts focus on social aspects ("friend", "help", "want"). Sentiment polarity differs significantly (mental health: 0.028 vs control: 0.071).

**Hypothesis:** Linguistic features can effectively discriminate between mental health and control posts.

### 2. **Network Centrality Patterns**
**Observation:** Hub subreddits show high degree centrality: ptsd (0.68), relationships (0.66), anxiety (0.64). Network density is 0.21 with a distinct core-periphery structure.

**Hypothesis:** Network structure reveals community importance beyond simple post volume.

### 3. **Extreme Engagement Skewness**
**Observation:** Highly skewed engagement distributions (score skewness: 11.04, comments: 8.98). Mental health posts receive significantly lower engagement (mean comments: 5.92 vs 15.74, p < 0.001).

**Hypothesis:** Engagement patterns require non-linear modeling approaches.

### 4. **Temporal Activity Patterns**
**Observation:** Mental health posts peak later (8 PM) compared to control posts (5 PM). Tuesday shows highest activity, with 25.2% of posts occurring on weekends.

**Hypothesis:** Temporal patterns reflect crisis-driven vs. situational posting motivations.

### 5. **Feature Dimensionality & Multicollinearity**
**Observation:** 116 features with strong multicollinearity concerns (e.g., post_length and word_count: r = 0.984).

**Hypothesis:** Dimensionality reduction can identify meaningful psychological constructs while improving model interpretability.

---

## Technical Approach

- **Text Mining:** TF-IDF vectorization, sentiment analysis, word frequency analysis
- **Clustering:** K-means clustering of users/posts, hierarchical topic clustering
- **Graph Mining:** Network centrality metrics, community detection algorithms
- **Statistical Testing:** Chi-square tests, Mann-Whitney U tests for group comparisons

---

## Primary Research Directions

1. **Classification Models:** Build interpretable models distinguishing mental health from control posts using linguistic, temporal, and network features
2. **Network Analysis:** Apply centrality measures and community detection to understand the support-seeking ecosystem
3. **Feature Engineering:** Identify optimal feature combinations balancing predictive accuracy and interpretability
4. **Engagement Modeling:** Investigate factors driving post visibility and community response patterns

---

## Repository Structure
```
├── 337002019_CheckPoint1.ipynb    # Checkpoint 1: Dataset selection, EDA, and hypothesis formulation
├── data/                          # (Excluded from repo) Raw CSV/JSON files
├── README.md                      # Project documentation
└── .gitignore                     # Excludes data files and sensitive content
```

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
- Extract files into a `data/` folder in the root directory

### 4. Run the Notebook
```bash
jupyter notebook 337002019_CheckPoint1.ipynb
```

---

## Ethical Considerations

This project handles sensitive mental health data with the following safeguards:

- **Anonymization:** All user identifiers are anonymized
- **No Personal Information:** Individual identification is prevented
- **Responsible Analysis:** Focus on aggregate patterns, not individual profiling
- **Academic Purpose:** Research is conducted for educational and public health insights
- **Bias Awareness:** Conscious effort to avoid stigmatizing language or conclusions

---

## Potential Applications

- **Crisis Detection Systems:** Early warning systems for mental health platforms
- **Community Moderation:** Identifying posts requiring professional intervention
- **Mental Health Research:** Understanding linguistic markers of different conditions
- **Platform Design:** Informing supportive features in social media applications
- **Public Health:** Population-level mental health trend monitoring


---

## Contact

**Author:** Aastha Patel  
**UIN:** 337002019  
**Course:** Data Mining Project at Texas A&M University  

---

## Acknowledgments

- Dataset providers on Kaggle
- Reddit API (PushShift) for historical data access

---

## License

This project is for academic purposes only. Please respect Reddit's terms of service and user privacy when working with social media data.

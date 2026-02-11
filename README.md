# Analyzing-Mental-Health-on-Social-Media
# Reddit Mental Health Analysis

**Analyzing Mental Health on Reddit**

This project investigates linguistic patterns in mental health communities on Reddit by combining classical data mining techniques (TF-IDF, clustering, graph analysis) with modern approaches (BERT embeddings, contextualized topic modeling). Our goal is to understand how mental health discourse differs from general conversation and build interpretable models while maintaining ethical safeguards.

## Dataset

- **Source:** Kaggle Reddit Mental Health Dataset
- **Size:** ~50K posts across 6 subreddits
- **Communities:** r/depression, r/Anxiety, r/SuicideWatch (mental health) + r/happy, r/CasualConversation
- **Features:** Post text, timestamps, engagement metrics, user interactions

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/reddit-mental-health-analysis.git
cd reddit-mental-health-analysis

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

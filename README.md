# Analyzing Mental Health on Social Media: Exploring Linguistic Patterns, Network Dynamics, and Crisis Detection in Online Mental Health Communities
## CSCE 676 Data Mining and Analysis Project — Texas A&M University

---

> 👉 **Start here:** [`main_notebook.ipynb`](./main_notebook.ipynb)

> 🎥 **Project Video:** [Watch here](https://youtu.be/DmndeI9yIbQ)

---

## Overview

This project applies data mining techniques to the Reddit Mental Health Corpus to uncover
linguistic patterns, community structures, and behavioral signals that distinguish mental health
communities from control communities on Reddit. Using Apriori, FP-Growth, conditioned
FP-Growth, and PrefixSpan sequential pattern mining, the project surfaces co-occurrence rules,
segment-level pattern differences, and ordered vocabulary dependencies across user post
histories. The findings have practical implications for content moderation, crisis detection
research, and mental health platform design.

---

## Research Questions

| # | Question | Method |
|---|----------|--------|
| RQ1 | What frequent word co-occurrence patterns emerge in mental health vs. control posts, and how do confidence and lift compare across varying support thresholds? | Apriori, FP-Growth |
| RQ2 | How do frequent co-occurrence patterns differ between behavioral segments (MH vs. control; daytime vs. late-night posters)? | Conditioned FP-Growth |
| RQ3 | Does ordering posts chronologically per user reveal sequential vocabulary dependencies that unordered itemset mining cannot detect? | PrefixSpan |

---

## Results Summary

- The strongest association rule in mental health posts is `panic -> attack` (lift 22.5), a tight
  clinical compound appearing 22x more often than chance would predict.
- Category-conditioned FP-Growth reveals 79-88 patterns invisible to a global model.
  Category segmentation is far more informative than temporal segmentation.
- PrefixSpan confirms vocabulary persistence as the dominant sequential structure: users
  repeatedly return to the same core vocabulary across posts, a signal unordered mining
  cannot detect.

---

## Dataset

**Name:** Reddit Mental Health Corpus  
**Source:** https://www.kaggle.com/datasets/ruchi798/stress-analysis-in-social-media  
**File:** `mental-health-data.csv`  
**Size:** 4,081 posts across 10 subreddits (5 mental health, 5 control)  
**Format:** CSV with 116 columns including raw text, LIWC scores, and engagement metrics

| Category | Subreddits |
|----------|-----------|
| Mental Health | anxiety, ptsd, stress, domesticviolence, survivorsofabuse |
| Control | relationships, assistance, homeless, almosthomeless, food_pantry |

The dataset is not committed to this repo due to file size. To reproduce:
1. Download `mental-health-data.csv` from the Kaggle link above
2. Upload it to your Google Drive at: `MyDrive/Data_Mining/mental-health-data.csv`
3. The notebook mounts Drive and loads it automatically

See [`data/README.md`](./data/README.md) for full preprocessing details.

---

## How to Reproduce

This project was built entirely in **Google Colab** with **Python 3.12.13**.

1. Clone or download this repo
2. Upload `mental-health-data.csv` to Google Drive at the path shown above
3. Open `main_notebook.ipynb` in Google Colab
4. Run all cells top to bottom — Runtime → Run all
5. All dependencies are installed automatically in the first cell

Full dependency list: [`requirements.txt`](./requirements.txt)

---

## Key Dependencies

| Package | Version |
|---------|---------|
| Python | 3.12.13 |
| pandas | 2.x |
| numpy | 1.x |
| scikit-learn | 1.4+ |
| mlxtend | 0.23+ |
| prefixspan | latest |
| nltk | 3.8+ |
| networkx | 3.x |
| matplotlib | 3.x |
| seaborn | 0.13+ |
| textblob | 0.18+ |
| scipy | 1.11+ |

---

## Repo Structure

```text
Analyzing-Mental-Health-on-Social-Media/
│
├── main_notebook.ipynb        ← Main deliverable: full analysis, start here
├── requirements.txt           ← Full Colab environment snapshot
├── README.md                  ← You are here
├── .gitignore
│
├── checkpoints/
│   ├── checkpoint_1.ipynb     ← Checkpoint 1: dataset selection and initial EDA
│   └── checkpoint_2.ipynb     ← Checkpoint 2: preprocessing and RQ development
│
└── data/
    └── README.md              ← Dataset source, download instructions, preprocessing notes
```

---

## Potential Applications

- **Crisis Detection:** Early warning systems for mental health platforms
- **Content Moderation:** Identifying posts requiring professional intervention
- **Mental Health Research:** Understanding linguistic markers across conditions
- **Platform Design:** Informing supportive features in social media applications
- **Public Health:** Population-level mental health trend monitoring

---

## Author

**Aastha Patel** | UIN: 337002019  
CSCE 676 Data Mining And Analysis
Texas A&M University

---

## Acknowledgments

- Reddit Mental Health Corpus dataset providers on Kaggle
- PushShift Reddit API for historical data access
- mlxtend and prefixspan open-source maintainers

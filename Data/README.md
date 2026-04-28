# Data

## Dataset

**Name:** Reddit Mental Health Corpus  
**Source:** https://www.kaggle.com/datasets/ruchi798/stress-analysis-in-social-media  
**File:** `mental-health-data.csv`  
**Size:** ~4,081 rows, 116 columns  

## Why this dataset was chosen

Three candidate datasets were evaluated. Twitter data was rejected due to the 280-character
limit restricting text richness. CounselChat was rejected due to small size (2K entries) and
lack of temporal or network dimensions. This Reddit corpus uniquely supports all three
research questions: it has long-form text, timestamps, engagement metrics, and community
structure.

## Subreddits

| Category | Subreddits |
|----------|-----------|
| Mental Health | anxiety, ptsd, stress, domesticviolence, survivorsofabuse |
| Control | relationships, assistance, homeless, almosthomeless, food_pantry |

## Preprocessing Steps

All preprocessing is performed in `main_notebook.ipynb` Section 4. Steps include:

1. Drop rows missing `text` or `subreddit`
2. Remove exact duplicate posts
3. Convert Unix timestamps to datetime and extract hour, day, month, is_weekend
4. Standardize subreddit names to lowercase
5. Map subreddits to `mental_health` or `control` category labels
6. Derive `word_count`, `post_length`, `engagement_rate` features
7. Assign synthetic `user_id` values for network and sequential analysis

## How to Access

The raw data file is not committed to this repo due to file size. Download it from Kaggle
and place it at this path in your Google Drive:
`MyDrive/Data_Mining/mental-health-data.csv`
The notebook mounts Drive automatically and loads from this path.
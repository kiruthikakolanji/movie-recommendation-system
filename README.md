# 🎬 Movie Recommendation System

A content-based movie recommendation web app that suggests similar movies based on genre, keywords, cast, and crew — built step by step using Python, Pandas, Scikit-learn, and Streamlit.

## 🚀 Live Demo
[Add your deployed app link here once deployed]

---

## 📌 Project Overview

A content-based movie recommendation system built on the **TMDB 5000 dataset**. It combines each movie's storyline, genre, keywords, top cast, and director into a single profile, then uses **Cosine Similarity** to find and recommend the 5 most similar movies — all through an interactive Streamlit web app.

---

## 🧠 Development Process — Step by Step

### Step 1: Setup & Get the Dataset
- Installed required libraries: `pandas`, `scikit-learn`, `streamlit`
- Downloaded the **TMDB 5000 Movie Dataset** from Kaggle (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`)
- Verified both files loaded correctly using `pandas.read_csv()`

### Step 2: Merge the Datasets
- Merged `movies` and `credits` datasets on the common `title` column using `.merge()`
- Combined dataset now had 23 columns from both files in one place

### Step 3: Select Important Columns
- Reduced the dataset to only the columns relevant for recommendations:
  `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`
- Checked for missing values using `.isnull().sum()`

### Step 4: Clean Missing Values & Parse Genres/Keywords
- Dropped rows with missing `overview` values
- Used Python's `ast.literal_eval()` to convert JSON-like genre/keyword strings into clean Python lists
  - Example: `'[{"name": "Action"}]'` → `['Action']`

### Step 5: Clean Cast & Crew Columns
- Extracted only the **top 3 cast members** per movie (main actors have the most influence on a movie's style)
- Extracted only the **director's name** from the crew list (filtered by `job == 'Director'`)

### Step 6: Combine Everything into a "Tags" Column
- Split `overview` into individual words
- Removed spaces within names (e.g., `"Sam Worthington"` → `"SamWorthington"`) to prevent incorrect partial-word matches
- Merged `overview`, `genres`, `keywords`, `cast`, and `crew` into a single `tags` column per movie

### Step 7: Finalize Dataset
- Kept only `movie_id`, `title`, and `tags` columns
- Converted `tags` from a list back into a single lowercase string (e.g., `"action adventure samworthington jamescameron..."`)

### Step 8: Convert Tags to Numbers & Calculate Similarity
- Used **CountVectorizer** (Bag of Words, top 5,000 features, English stopwords removed) to convert each movie's tags into a numerical vector
- Calculated **Cosine Similarity** between every pair of movies, producing a 4,806 × 4,806 similarity matrix

### Step 9: Build the Recommend Function
- Wrote a `recommend()` function that:
  1. Finds a movie's index in the dataset
  2. Retrieves its similarity scores with all other movies
  3. Sorts by similarity (highest first) and returns the top 5 matches
- Tested with `recommend('Avatar')` → returned relevant sci-fi/space movies ✅

### Step 10: Save the Model
- Saved the cleaned dataset (`movies.pkl`) and similarity matrix (`similarity.pkl`) using `pickle`
- Compressed the similarity matrix with `gzip` (184MB → 39MB) to stay within GitHub's file size limits

### Step 11: Build the Streamlit Web App
- Built `app.py` with a dropdown (`st.selectbox`) to choose a movie and a button to trigger recommendations
- Loaded the saved model files and displayed the top 5 recommended movies on the page

### Step 12: Push to GitHub
- Initialized Git, connected to a GitHub repository, and pushed all project files using Git command line
- Resolved a merge conflict between local and remote files using `git pull --allow-unrelated-histories -X ours`

### Step 13: Deploy
- Deployed the app on **Streamlit Cloud**, connected directly to the GitHub repository
- Verified the live app works with real-time movie recommendations

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🐼 Pandas | Data merging, cleaning, and manipulation |
| 🤖 Scikit-learn | CountVectorizer & Cosine Similarity |
| 🎈 Streamlit | Web app interface |
| 🔧 Git & GitHub | Version control and deployment |

## 📊 Dataset
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) – 4,800+ movies with genres, keywords, cast, and crew information

## 📈 Model Performance / Output Quality
Tested with sample inputs (e.g., "Avatar", "Iron Man 2") and consistently returned genre-accurate, contextually relevant recommendations.

## 💻 How to Run Locally

1. Clone this repository
```bash
git clone https://github.com/kiruthikakolanji/movie-recommendation-system.git
cd movie-recommendation-system
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
python -m streamlit run app.py
```

## 📁 Project Structure

| File | Description |
|---|---|
| 📄 `app.py` | Streamlit web app — UI and recommendation logic |
| 📄 `test.py` | Model training script (data cleaning → similarity matrix) |
| 📦 `movies.pkl` | Cleaned movie dataset (titles + tags) |
| 📦 `similarity.pkl.gz` | Compressed cosine similarity matrix |
| 📊 `tmdb_5000_movies.csv` | Original movie dataset |
| 📊 `tmdb_5000_credits.csv` | Original cast & crew dataset |
| 📋 `requirements.txt` | Python dependencies |
| 📖 `README.md` | Project documentation |

## 🎯 Future Improvements
- Add movie posters using the TMDB API
- Include collaborative filtering based on user ratings
- Add search/filter by genre

## 👤 Author
Kiruthika Kolanji – [LinkedIn Profile Link]

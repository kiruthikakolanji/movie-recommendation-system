# 🎬 Movie Recommendation System

A content-based movie recommendation web app that suggests similar movies based on genre, keywords, cast, and crew using Natural Language Processing and Cosine Similarity.

## 🚀 Live Demo
[Add your deployed app link here once deployed]

## 📋 Features
- Get 5 personalized movie recommendations instantly
- Content-based filtering (genre, storyline, cast, director)
- Clean, simple dropdown interface

## 🛠️ Tech Stack
- **Python** – Core programming language
- **Pandas** – Data manipulation and merging
- **Scikit-learn** – CountVectorizer & Cosine Similarity
- **Streamlit** – Web app interface
- **Git & GitHub** – Version control

## 📊 Dataset
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) – 4,800+ movies with genres, keywords, cast, and crew information

## 🧠 How It Works
1. Movie and credits datasets are merged on title
2. Genres, keywords, cast (top 3), and director are extracted and cleaned
3. All features are combined into a single "tags" column per movie
4. Tags are converted to numerical vectors using CountVectorizer
5. Cosine Similarity calculates how alike every movie is to every other movie
6. Top 5 most similar movies are returned for any selected movie

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

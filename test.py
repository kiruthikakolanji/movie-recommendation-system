import pandas as pd

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title')
print("After merging:", movies.shape)
print(movies.columns.tolist())

movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
print(movies.head())

print("\nMissing values:\n", movies.isnull().sum())


import ast
movies.dropna(inplace=True)

def convert(text):
    names = []
    for item in ast.literal_eval(text):
        names.append(item['name'])
    return names

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
print(movies[['title', 'genres', 'keywords']].head())

def convert_cast(text):
    names = []
    count = 0
    for item in ast.literal_eval(text):
        if count < 3:
            names.append(item['name'])
            count += 1
        else:
            break
    return names
movies['cast'] = movies['cast'].apply(convert_cast)

def fetch_director(text):
    names = []
    for item in ast.literal_eval(text):
        if item['job'] == 'Director':
            names.append(item['name'])
            break
    return names
movies['crew'] = movies['crew'].apply(fetch_director)
print(movies[['title', 'cast', 'crew']].head())

movies['overview'] = movies['overview'].apply(lambda x: x.split())

def remove_space(word_list):
    return [i.replace(" ", "") for i in word_list]

movies['genres'] = movies['genres'].apply(remove_space)
movies['keywords'] = movies['keywords'].apply(remove_space)
movies['cast'] = movies['cast'].apply(remove_space)
movies['crew'] = movies['crew'].apply(remove_space)

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
print(movies[['title', 'tags']].head())

new_df = movies[['movie_id', 'title', 'tags']]

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

print(new_df.head())
print("\nExample tag for Avatar:\n", new_df['tags'][0])



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()
print("Shape of vectors:", vectors.shape)

similarity = cosine_similarity(vectors)
print("Shape of similarity matrix:", similarity.shape)
print("\nSimilarity scores for Avatar (first 5):", similarity[0][:5])


def recommend(movie):
    
    movie_index = new_df[new_df['title'] == movie].index[0]
    
    distances = similarity[movie_index]
    
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    for i in movie_list:
        print(new_df.iloc[i[0]].title)

print("Movies similar to Avatar:\n")
recommend('Avatar')



import pickle
import gzip

with gzip.open('similarity.pkl.gz', 'wb') as f:
    pickle.dump(similarity, f)

pickle.dump(new_df, open('movies.pkl', 'wb'))

print("Files saved successfully (compressed)!")


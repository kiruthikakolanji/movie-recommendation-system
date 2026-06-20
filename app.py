import streamlit as st
import pickle
import gzip

movies = pickle.load(open('movies.pkl', 'rb'))

with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get 5 similar recommendations!")

selected_movie = st.selectbox("Choose a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("You might also like:")
    for movie in recommendations:
        st.write("🎥", movie)
        
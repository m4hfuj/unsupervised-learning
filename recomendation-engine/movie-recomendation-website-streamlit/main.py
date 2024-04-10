import streamlit as st
import pandas as pd
import pickle


movies_list = pd.DataFrame(pickle.load(open("movies.pkl", "rb")))
similarity_matrix = pd.DataFrame(pickle.load(open("similarity_matrix.pkl", "rb")))

def make_rocommendation(movie_name):
    recommended_movies = []
    similar_scores = similarity_matrix[movie_name]
    similar_scores = pd.DataFrame(similarity_matrix[movie_name])
    similar_scores = similar_scores.sort_values(movie_name, ascending=False)[1:11]
    # similar_scores = similar_scores.rename(columns={movie_name: "similarity_index"})
    similar_scores = similar_scores.merge(movies_list, on="title")
    for m in similar_scores["title"]:
        recommended_movies.append(m)
    return recommended_movies




st.title("Movie Recomender System")

option = st.selectbox(
    'Select a movie you like',
    (movies_list["title"].values))

st.write("Your Selected Movie:", option)

if st.button("Recommend"):
    recommendations = make_rocommendation(option)
    # st.write('You selected:', option)
    for movie in recommendations:
        st.write(movie)
    

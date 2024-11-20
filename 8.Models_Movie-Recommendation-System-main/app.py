import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.markdown("<h1 style='text-align: center; color: black;'>Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Find a similar movie from a dataset of 5,000 movies!</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Web App created by Ashish Sinha</h4>", unsafe_allow_html=True)

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie you like:",
    movie_list
)

if st.button('Show Recommendation'):
    st.write("Recommended Movies based on your interests are:")
    recommended_movie_names = recommend(selected_movie)
    for movie in recommended_movie_names:
        st.text(movie)

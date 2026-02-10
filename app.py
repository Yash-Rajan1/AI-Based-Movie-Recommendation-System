import streamlit as st
import pickle
import os
import requests
import gdown

# https://drive.google.com/file/d/19akgab2plarRI-ehmBdfJAZvkPKsQG52/view?usp=drive_link
file_id = '19akgab2plarRI-ehmBdfJAZvkPKsQG52'
url = f'https://drive.google.com/uc?id={file_id}'
output = 'similarity.pkl'
if not os.path.exists(output):
    with st.spinner('Downloading similarity matrix... this might take a minute.'):
        gdown.download(url,output,quiet=False)
API_KEY = st.secrets["tmdb_api_key"]

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        data = requests.get(url).json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except:
        return "https://via.placeholder.com/500x750"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_posters

similarity = pickle.load(open(output,'rb'))

movies = pickle.load(open('movies.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie would you like a recommendation for?',movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    # create 5 cols
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])

            st.image(posters[i])



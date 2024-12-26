import streamlit as st
import pickle
import requests
st.header('Movie Recommender')
movies_list=pickle.load(open('movies_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


movies_list_title=movies_list['title'].values
select_value=st.selectbox("Select movies from dropdown",movies_list_title)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=3f8a3d4ca5c836c11cab74f3f26bb203&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path
def recommand(movies):
    index = movies_list[movies_list['title'] == movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommeneded_movies = []
    recommended_poster = []
    for i in distance[1:6]:
        movie_id = movies_list.iloc[i[0]].id
        recommeneded_movies.append(movies_list.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))  # Fetch the poster URL here
    return recommeneded_movies, recommended_poster

if st.button('Show Recommended'):
  movies_recommended,recommended_poster=recommand(select_value)
  col1,col2,col3,col4,col5=st.columns(5)
  with col1:
    st.text(movies_recommended[0])
    st.image(recommended_poster[0])
  with col2:
    st.text(movies_recommended[1])
    st.image(recommended_poster[1])
  with col3:
    st.text(movies_recommended[2])
    st.image(recommended_poster[2])
  with col4:
    st.text(movies_recommended[3])
    st.image(recommended_poster[3])
  with col5:
    st.text(movies_recommended[4])
    st.image(recommended_poster[4])
    

  




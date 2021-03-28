import pandas as pd
from model import model
from itertools import islice
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('training_dataset/IMDb movies.csv')

cosine_sim = model.get_model()

def get_movie_from_index(index):
    return df[df.index == index].to_dict('records')[0]

def get_index_from_title(title):
    return df[df.title.str.lower() == title.lower()]['index'].values[0]

def get_index_from_imdb_id(imdb_id):
    return df[df.imdb_title_id == imdb_id]['index'].values[0]

def recommend_movies(movie_user_likes, imdb_id, number_of_recommendations):
    if imdb_id and imdb_id in df.imdb_title_id.str:
        movie_index = get_index_from_imdb_id(imdb_id)
    elif movie_user_likes and movie_user_likes.lower() in df.title.str.lower().unique():
        movie_index = get_index_from_title(str(movie_user_likes))
    else:
        return 'Movie not in Database'
    
    similar_movies =  list(enumerate(cosine_sim[movie_index]))

    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

    movies = (get_movie_from_index(element[0]) for element in sorted_similar_movies)
    recommended_movies = list(islice(movies, int(number_of_recommendations)))

    return recommended_movies

import os
import pandas as pd
from ml_model import ml_model
from itertools import islice
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dataset = pd.read_csv(os.environ.get('DATASET_PATH', os.path.join(BASE_DIR, 'training_dataset/IMDb movies.csv')))

trained_model = ml_model.get_model()

def get_movie_from_index(index):
    return dataset[dataset.index == index].to_dict('records')[0]

def get_index_from_title(title):
    return dataset[dataset.title.str.lower() == title.lower()]['index'].values[0]

def get_index_from_imdb_id(imdb_id):
    return dataset[dataset.imdb_title_id == imdb_id]['index'].values[0]

def recommend_movies(query):
    if query['q'] in dataset.imdb_title_id.str.lower().unique():
        movie_index = get_index_from_imdb_id(query['q'])
    elif query['q'].lower() in dataset.title.str.lower().unique():
        movie_index = get_index_from_title(query['q'])
    else:
        return query, [], 404, 'Movie not in Database.'
    
    similar_movies =  list(enumerate(trained_model[movie_index]))

    sorted_similar_movies = sorted(similar_movies, key = lambda x:x[1], reverse = True)[1:]

    movies = (get_movie_from_index(element[0]) for element in sorted_similar_movies)
    recommended_movies = list(islice(movies, query['limit']))

    return query, recommended_movies, 200, ''

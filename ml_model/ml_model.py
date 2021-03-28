import numpy as np
import os
import pandas as pd
from os import path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def train_model():
    dataset = pd.read_csv('training_dataset/IMDb movies.csv')
    features = ['keywords', 'cast', 'genres', 'director']

    def combine_features(row):
        return row['keywords'] + ' ' + row['cast']+ ' ' + row['genres']+ ' ' + row['director']

    for feature in features:
        dataset[feature] = dataset[feature].fillna('')

    dataset['combined_features'] = dataset.apply(combine_features, axis=1)
    dataset = dataset.filter(['combined_features'])

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(dataset['combined_features'])
    ml_model = cosine_similarity(count_matrix)

    np.save('ml_model/ml_model.npy', ml_model)

    return ml_model

def get_model():
    if path.exists('ml_model/ml_model.npy'):
        return np.load('ml_model/ml_model.npy')
    else:
        return train_model()

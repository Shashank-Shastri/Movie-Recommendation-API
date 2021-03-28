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
    model = cosine_similarity(count_matrix)

    np.save('model/model.npy', model)

    return model

def get_model():
    if path.exists('model/model.npy'):
        return np.load('model/model.npy')
    else:
        return train_model()

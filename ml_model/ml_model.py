import numpy as np
import os
import pandas as pd
from os import path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def train_model():
    dataset = pd.read_csv(os.environ.get('DATASET_PATH', os.path.join(BASE_DIR, 'training_dataset/IMDb movies.csv')))
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
    if path.exists(os.path.join(BASE_DIR, 'ml_model/ml_model.npy')):
        return np.load(os.path.join(BASE_DIR, 'ml_model/ml_model.npy'))
    elif os.environ.get('ML_MODEL_PATH', False):
        return np.load(os.environ.get('ML_MODEL_PATH', False))
    else:
        return train_model()

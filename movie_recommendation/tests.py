from django.test import TestCase
from .recommendation import recommend_movies


class RecommendMoviesTestCase(TestCase):
    def test_recommendation_by_id(self):
        """Movie Recommendations are correctly listed"""
        movie_imdb_id = "tt0499549"
        result_limit = 5

        query = {
            'limit': result_limit,
            'q': movie_imdb_id
        }

        result, status, error = recommend_movies(query)

        self.assertEqual(status, 200)
        self.assertEqual(error, '')
        self.assertEqual(len(result), 5)

    def test_limiting_results(self):
        """Movie Recommendations are correctly listed"""
        movie_imdb_id = "tt0499549"
        result_limit = 0

        query = {
            'limit': result_limit,
            'q': movie_imdb_id
        }

        result, status, error = recommend_movies(query)

        self.assertEqual(status, 200)
        self.assertEqual(error, '')
        self.assertEqual(len(result), 0)

    def test_recommendation_by_title(self):
        """Movie Recommendations are correctly listed"""
        movie_title = "The Hobbit: The Battle of the Five Armies"
        result_limit = 15

        query = {
            'limit': result_limit,
            'q': movie_title
        }

        result, status, error = recommend_movies(query)

        self.assertEqual(status, 200)
        self.assertEqual(error, '')
        self.assertEqual(len(result), 15)

    def test_recommendation_is_empty(self):
        """404 is returned"""
        movie_title = "Star Trek Nemesis"
        result_limit = 5

        query = {
            'limit': result_limit,
            'q': movie_title
        }

        result, status, error = recommend_movies(query)

        self.assertEqual(status, 404)
        self.assertEqual(error, 'Movie not in Database.')
        self.assertEqual(len(result), 0)

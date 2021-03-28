from django.http import HttpResponse, JsonResponse
from . import recommendation
from ml_model import ml_model

def recommend_movies(request):
    movie_name = request.GET.get('title') or False
    imdb_id = request.GET.get('imdb_id') or False
    number_of_recommendations = request.GET.get('limit') or 5

    return JsonResponse(recommendation.recommend_movies(movie_name, imdb_id, number_of_recommendations), safe=False)

def retrain_model(request):
    ml_model.train_model()
    return HttpResponse('Model Retrained.')

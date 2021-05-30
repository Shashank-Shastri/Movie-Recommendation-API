from django.http import HttpResponse, JsonResponse
from . import recommendation
from ml_model import ml_model


def recommend_movies(request):
    movie_name = request.GET.get('title', '')
    imdb_id = request.GET.get('imdb_id', '')
    limit = request.GET.get('limit', 5)

    query = {
        'limit': int(limit),
        'q': imdb_id or movie_name,
        'type': 'imdb_id' if imdb_id else 'title' if movie_name else ''
    }

    if query['q']:
        query, result, status, error = recommendation.recommend_movies(query)
    else:
        error = 'Empty query.'
        result = []
        status = 400

    response = {
        'query': query,
        'result': result
    }

    if error:
        response['error'] = error

    return JsonResponse(status=status, data=response)


def retrain_model(request):
    ml_model.train_model()
    return HttpResponse('Model Retrained.')

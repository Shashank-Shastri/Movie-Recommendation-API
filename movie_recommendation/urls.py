from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recommend_movies', views.recommend_movies, name='recommend_movies'),
    url(r'^retrain_model', views.retrain_model, name='retrain_model'),
]

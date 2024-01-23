from django.urls import path
from .views import *


urlpatterns = [
    # route is a string contains a URL pattern
    path('', movie_recommender, name='movie_recommender'),

]

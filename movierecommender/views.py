from . import views
from .models import Movie
from django.shortcuts import render

# HINT: Create a view to provide movie recommendations list for the HTML template


def generate_movies_context():
    context = {}
    # Show only movies in recommendation list
    # Sorted by vote_average in desc
    # Get recommended movie counts
    recommended_count = Movie.objects.filter(
        recommended=True
    ).count()
    # If there are no recommended movies
    if recommended_count == 0:
        # Just return the top voted and unwatched movies as popular ones
        movies = Movie.objects.filter(
            watched=False
        ).order_by('-vote_count')[:30]
    else:
        # Get the top voted, unwatched, and recommended movies
        movies = Movie.objects.filter(
            watched=False
        ).filter(
            recommended=True
        ).order_by('-vote_count')[:30]
    context['movie_list'] = movies
    return context

def movie_recommender(request):

    # Generates the context dictionary with movie data to pass to the template.
    # Gets recommended movies or popular movies if no recommendations.
    context = generate_movies_context()


    # Renders the movie recommendation page by generating the context 
    # with movie data and passing it to the template.
    return render(request, 'movierecommender/movie_list.html', context=context)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Score
# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html',{
        'movies': movies
    })

def movie_detail(request, movie_id) :
    movie = get_object_or_404(Movie, id=movie_id)
    scores = movie.score_set.all()
    return render(request, 'movies/detail.html',{
        'movie' : movie,
        'scores' : scores
    })

def delete_movie(request, movie_id) :
    if request.method == 'POST' :
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
    return redirect('movies:movie_list')

def create_score(request, movie_id) :
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        score = Score()
        score.score = request.POST.get('score')
        score.content = request.POST.get('content')
        score.movie_id = movie.id
        score.save()
    return redirect('movies:movie_detail',movie.id)


def delete_score(request, movie_id, score_id) :
    if request.method == 'POST' :
        score = get_object_or_404(Score, id=score_id)
        score.delete()

    return redirect('movies:movie_detail', movie_id)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Score
from .forms import MovieModelForm
from django.contrib import messages

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

def new(request) :
    if request.method == "POST" :
        form = MovieModelForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('movies:movie_detail', form.instance.id)
    else :
        # form을 보여준다.
        form = MovieModelForm()
    return render(request, 'movies/form.html', {'form':form})

def edit_movie(request, movie_id) :
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST' :
        # 저장
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid() :
            form.save()
            return redirect('movies:movie_detail', form.instance.id)
        messages.success(request, '유효하지 않은 데이터입니다.')
    else :
        # 수정페이지
        form = MovieModelForm(instance=movie)
    return render(request, 'movies/form.html', {'form':form})
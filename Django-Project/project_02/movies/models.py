from django.db import models

# Create your models here.
class Genre(models.Model) :
    name = models.TextField(default='')

class Movie(models.Model) :
    title = models.TextField(default="")
    audience = models.IntegerField()
    poster_url = models.TextField(default = '')
    description =models.TextField(default='')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Score(models.Model) :
    content = models.TextField(default='')
    score = models.IntegerField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
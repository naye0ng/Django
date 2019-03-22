from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name = 'movie_list'),
    path('<int:movie_id>/', views.movie_detail, name= 'movie_detail'),
    path('<int:movie_id>/delete/', views.delete_movie, name= 'delete_movie'),
    path('<int:movie_id>/scores/new', views.create_score, name='create_score'),
    path('<int:movie_id>/scores/<int:score_id>/delete', views.delete_score, name='delete_score'),
    path('new/',views.new, name='new'),
    path('<int:movie_id>/edit/', views.edit_movie, name='edit_movie'),
]

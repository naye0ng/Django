from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path('',views.article_list,name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    # path('new/',views.new_article, name = 'new_article'),
    path('create/',views.create_article,name='create_article'),
    path('<int:article_id>/update/',views.update_article, name= 'update_article'),
    path('<int:article_id>/delete/',views.delete_article, name='delete_article'),
    # board/1/comment/create
    path('<int:article_id>/comments/create',views.create_comment,name='create_comment'),
    # board/1/comment/1/delete
    path('<int:article_id>/comments/<int:comment_id>/delete',views.delete_comment,name='delete_comment'),
]
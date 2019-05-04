from django.urls import path
from . import views
from .models import Movie

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies/<slug:movie_title>', views.post_movie, name="postMovie"),
    path('comments/', views.comments, name="comments"),
    path('comments/<int:movieID>', views.comments_for_movie, name="comment_for_movie"),
    path('comments/<int:movieID>/<slug:comment_text>', views.post_comments, name="postComment"),
    path('top/<int:year>/<int:month>/', views.get_top, name="topMoviesByComments"),
]
from django.db import models
import datetime


class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_ID = models.IntegerField(primary_key=True)
    rank = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    def __str__(self):
    	return self.movie_title + str(self.total_comments) + str(self.rank)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
    def __str__(self):
    	return self.comment_text + str(self.pub_date)
from django.http import HttpResponse
from .models import Movie, Comment
import requests as req

def index(request):
    return HttpResponse("Hello, world. NetguruMovieDB index.")

def movies(request):
    movielist = Movie.objects.all()

    return HttpResponse(movielist)

def post_movie(request, movie_title):
	#cast
	movie_title = str(movie_title)
	m = Movie(movie_title)
	#guard
	if(verify_movie_exists(movie_title)):
		return HttpResponse("movie found internally")
	#api request
	response_text = get_movie_details_ext(movie_title)
	#m.save() #no need to duplicate information. we pull info from ext API, and only save references (aka movie title) PROBLEM HERE
	if ("Movie not found externally" in response_text):
		return HttpResponse(response_text)
	#response: full movie object json(); (with data from ext api)
	return HttpResponse(response_text)

def comments(request):
	commentlist = Comment.objects.all()
	return HttpResponse(commentlist)

def comments_for_movie(request, movieID):
	if (verify_movie_exists_by_id(movieID)):
		return HttpResponse("movie does not exist internally")
	commentlist = Comment.objects.filter(movie__movie_ID=movieID)
	if(commentlist.count() < 1):
		return HttpResponse("no comments for this movie")
	return HttpResponse(commentlist)

def post_comments(request, comment_text, movieID):
	#if not there, return error
	if (verify_movie_exists_by_id(movieID)):
		return HttpResponse("data; comment_text: " + comment_text + " movie does not exist (id: " + str(movieID) + ")")
	movie = Movie.objects.get(movie_ID=movieID)
	c = Comment(comment_text=comment_text, movie=movie)
	c.save()
	movie.total_comments +=1
	movie.save()
	return HttpResponse("data; comment object: " + str(c))

def get_top(request, year, month):
	
	movielist = Movie.objects.order_by("-total_comments")
	return HttpResponse(movielist + str(year))

def verify_movie_exists_by_id(id):
	movie_from_db = Movie.objects.filter(movie_ID=id)
	if(movie_from_db.count() < 1):
		return True
	return False

def verify_movie_exists(title):
	movie_from_db = Movie.objects.filter(movie_title=title).exists()
	if (movie_from_db):
		return True
	return False

def get_movie_details_ext(title):
	payload = {'apikey':'666bfd5e', 't': title}
	response = req.get("http://www.omdbapi.com/", params=payload)
	if("False" in response.text): #not a good way to do it ...
		return "Movie not found externally"
	return response.text
from django.shortcuts import render
import requests
import json

# Create your views here.

f = open("key.txt", "r")
key = f.read()
f.close()

def home(request):
	return render(request, 'home.html',{} )

def movieslist(request):
	movie = request.POST['movie']
	movie_request = requests.get("http://www.omdbapi.com/?s="+movie+"&apikey="+key)
	api = json.loads(movie_request.content)
	return render(request,'movieslist.html',{'api':api, 'movie':movie})


def moviedetails(request,single_slug):
	movie_request = requests.get("http://www.omdbapi.com/?i="+single_slug+"&apikey="+key)
	api = json.loads(movie_request.content)
	return render(request, 'moviedetails.html',{'api':api} )
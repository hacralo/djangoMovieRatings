from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('movieslist/', views.movieslist, name='movieslist'),
        path('<single_slug>', views.moviedetails, name='moviedetails')
]

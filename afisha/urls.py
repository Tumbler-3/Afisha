"""afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie_app.views import (DirectorViewAPI, DirectorDetailViewAPI, 
                             MovieViewAPI, MovieDetailViewAPI, MovieReviewViewAPI,
                             RevieViewAPI, ReviewDetailViewAPI) 

from . import yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/directors/', DirectorViewAPI.as_view()),
    path('api/v1/directors/<int:id>/', DirectorDetailViewAPI.as_view()),

    path('api/v1/movies/', MovieViewAPI.as_view()),
    path('api/v1/movies/<int:id>/', MovieDetailViewAPI.as_view()),
    path('api/v1/movies/reviews/', MovieReviewViewAPI.as_view()),
    
    path('api/v1/reviews/', RevieViewAPI.as_view()),
    path('api/v1/reviews/<int:id>/', ReviewDetailViewAPI.as_view()),
    
    path('api/v1/profiles/', include('profiles.urls'))
]


urlpatterns += yasg.urlpatterns
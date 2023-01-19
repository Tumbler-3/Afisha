from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import (DirectorSerializer, DirectorDetailSerializer, 
                          MovieSerializer, MovieDetailSerializer, 
                          ReviewSerializer, ReviewDetailSerializer,
                          MovieReviewSerializer)

@api_view(['GET'])
def director_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_detail_view(request, id):
    director = Director.objects.get(id=id)
    serializer = DirectorDetailSerializer(director, many=False)
    return Response(data=serializer.data)



@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_detail_view(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieDetailSerializer(movie, many=False)
    return Response(data=serializer.data)



@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    serializer = ReviewDetailSerializer(review, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_review_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(movies, many=True)
    return Response(data=serializer.data)
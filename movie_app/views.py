from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView ,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Director, Movie, Review
from .serializers import (DirectorSerializer, DirectorDetailSerializer, DirectorValidatorSerializer,
                          
                          MovieSerializer, MovieDetailSerializer, MovieValidatorSerializer,
                          
                          ReviewSerializer, ReviewDetailSerializer, ReviewValidatorSerializer,
                          
                          MovieReviewSerializer)


class DirectorViewAPI(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination
    
    def create(self, request, *args, **kwargs):
        serializer = DirectorValidatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        name = serializer.validated_data.get('name')
        
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)



class DirectorDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer
    lookup_field = 'id'


class MovieViewAPI(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    
    def create(self, request, *args, **kwargs):
        serializer = MovieValidatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
    

class MovieDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'


class MovieReviewViewAPI(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = PageNumberPagination


class RevieViewAPI(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    
    def create(self, request, *args, **kwargs):
        serializer = ReviewValidatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
    

class ReviewDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = 'id'
    
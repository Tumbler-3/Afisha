from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ('name', 'movies_count')
        
    def get_movies_count(self, director_object):
        movies_count = director_object.director_movie.all()
        movies = 0
        for i in movies_count:
            movies+=1
        return movies


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'duration')


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('stars', 'text')


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    movie_review = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('title', 'movie_review', 'rating')

    def get_rating(self, movie_object):
        movie_review = movie_object.movie_review.all()
        rate = 0
        count = 0
        for i in movie_review:
            count += 1
            rate += i.stars
        try: 
            rate = rate/count
            return rate
        except:
            return 0 

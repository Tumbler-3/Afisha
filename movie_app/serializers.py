from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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


class DirectorValidatorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'duration')


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField()
    duration = serializers.DurationField()
    director_id = serializers.IntegerField(min_value=1)
    
    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with {director_id} id does not exists')
        return director_id


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('stars', 'text', 'movie')


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        

class ReviewValidatorSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    
    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError(f'Movie with {movie_id} id does not exists')
        return movie_id


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

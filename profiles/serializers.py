from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

class AuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    

class RegistrationSerializer(AuthorizationSerializer):
    
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('Username alredy exists')
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from profiles.serializers import AuthorizationSerializer, RegistrationSerializer


@api_view(['POST'])
def authorization(request):
    serializer = AuthorizationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    
    return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)
from django.urls import path
from profiles.views import AuthorizationViewAPI, RegistrationViewAPI


urlpatterns = [
    path('authorization/', AuthorizationViewAPI.as_view()),
    path('registration/', RegistrationViewAPI.as_view())
]

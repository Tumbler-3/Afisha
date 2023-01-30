from django.urls import path
from profiles.views import authorization, registration


urlpatterns = [
    path('authorization/', authorization),
    path('registration/', registration)
]

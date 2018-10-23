# users/urls.py

from django.urls import path
from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
    path('token/',authenticate_user),
]
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from account.api import RegisterApi

app_name = 'account'
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', RegisterApi.as_view(), name='register'),
]

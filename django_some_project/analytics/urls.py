from django.urls import path

from analytics.api import LikesStatisticView, UserStatisticView

app_name = 'analytics_api'
urlpatterns = [
    path('likes/', LikesStatisticView.as_view(), name='likes'),
    path('user/<str:username>/', UserStatisticView.as_view(), name='user'),
]

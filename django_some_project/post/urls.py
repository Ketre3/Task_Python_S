from django.urls import path
from post.api import (
    AllPostsView,
    LikePostView,
    CreatePostView,
    RetrievePostView,
)


app_name = 'post_api'
urlpatterns = [
    path('all/', AllPostsView.as_view(), name='all'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('<int:pk>/', RetrievePostView.as_view(), name='post'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like'),
]

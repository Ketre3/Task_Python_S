from django.urls import path, include

api_urls = [
    path('post/', include('post.urls', 'post_api')),
    path('analytics/', include('analytics.urls', 'analytics_api')),
    path('account/', include('account.urls', 'account_api')),
]

urlpatterns = [
    path('api/', include(api_urls)),
]

from django.urls import path
from .views import RedditPostView

urlpatterns = [
    path('reddit-post-data', RedditPostView.as_view(), name='reddit-post-data')
]
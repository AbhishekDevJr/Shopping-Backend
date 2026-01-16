from rest_framework import serializers
from .models.RedditPosts import RedditPosts
from .models.RedditComments import RedditComments

class RedditPostCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    body = serializers.CharField()
    category = serializers.CharField()
    sub_reddit_name = serializers.CharField()
    upvote_ratio = serializers.FloatField()
    post_url = serializers.URLField()
    
    class Meta:
        model = RedditPosts
        fields = ['title', 'body', 'category', 'sub_reddit_name', 'upvote_ratio', 'post_url']
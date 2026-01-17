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
        
        
class RedditCommentPostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    body = serializers.CharField()
    category = serializers.CharField()
    reddit_post = serializers.PrimaryKeyRelatedField(
        queryset = RedditPosts.objects.all()
    )
    sub_reddit_name = serializers.CharField()
    upvote_ratio = serializers.FloatField()
    
    class Meta:
        model = RedditComments
        fields = ['title', 'body', 'category', 'reddit_post', 'sub_reddit_name', 'upvote_ratio']
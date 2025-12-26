from django.db import models
from .RedditPosts import RedditPosts

class RedditComments(models.Model):
    title = models.CharField(null=False, blank=False, db_column="POST_COMMENT")
    body = models.TextField(null=False, blank=False, db_column="COMMENT_BODY")
    reddit_post = models.ForeignKey(RedditPosts, related_name="post_comments", on_delete=models.CASCADE, db_column="REDDIT_POST_FK")
    sub_reddit_name = models.CharField(null=False, blank=False, db_column="SUB_REDDIT_NAME")
    upvote_ratio = models.FloatField(null=False, blank=False, db_column="COMMENT_UPVOTE_SCORE")
    comment_url = models.URLField(null=True, blank=True, db_column="COMMENT_URL")
    created_at = models.DateField(null=False, blank=False, db_column="COMMENT_CREATED_DATE")
    
    class Meta:
        pass
    
    def __str__(self):
        return f"{self.title} - {self.comment_url}"
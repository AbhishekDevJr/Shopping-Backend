from django.db import models
from ..constants import CATEGORY_CHOICES

class RedditPosts(models.Model):
    title = models.CharField(null=False, blank=False, db_column="POST_TITLE")
    body = models.TextField(null=False, blank=False, db_column="POST_BODY")
    category = models.TextField(null=False, blank=False, choices=CATEGORY_CHOICES, db_column="POST_CATEGORY")
    sub_reddit_name = models.CharField(null=False, blank=False, db_column="SUB_REDDIT_NAME")
    upvote_ratio = models.FloatField(null=False, blank=False, db_column="POST_UPVOTE_SCORE")
    post_url = models.URLField(null=True, blank=True, db_column="POST_URL")
    created_at = models.DateField(null=False, blank=False, db_column="POST_CREATED_DATE", auto_now=True)
    
    class Meta:
        pass
    
    def __str__(self):
        return f"{self.title} - {self.post_url}"
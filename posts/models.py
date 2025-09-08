from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    # author = models.CharField(max_length=50)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="author-post"
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

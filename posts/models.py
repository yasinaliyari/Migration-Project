from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=True)


class Post(models.Model):
    STATUS_CHOICES = (
        ("d", "draft"),
        ("p", "published"),
    )
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="author"
    )
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category"
    )
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="d")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

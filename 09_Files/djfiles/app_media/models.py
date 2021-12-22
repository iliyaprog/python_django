from django.contrib.auth.models import User
from django.db import models


class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, max_length=500)
    created_ap = models.DateTimeField(auto_now_add=True)


class FeedFile(models.Model):
    file = models.ImageField(upload_to='files/')
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='files')







from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="exclusiveImages/")
    video = models.FileField(null=True, blank=True, upload_to="exclusiveVids/")
    caption = models.CharField(max_length=511)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

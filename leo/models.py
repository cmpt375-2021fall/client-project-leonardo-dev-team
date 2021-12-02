from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="exclusiveImages/")
    video = models.FileField(null=True, blank = True, upload_to="exclusiveVids/")
    caption = models.CharField(max_length=511)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Calender(models.Model):
    title = models.CharField(max_length=255)
    calenderLink = models.CharField(max_length=511)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="NewsImages/")
    body = models.TextField()
    post_date = models.DateField(default=datetime.now)
    link = models.CharField(max_length=511, null= True, blank=True)

    def __str__(self):
        return self.title


class MembershipInfo(models.Model):
    cardholderOne = models.CharField(max_length=255)
    cardholderTwo = models.CharField(max_length=255)
    LookupID = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    MemberID = models.CharField(max_length=255)
    MemberSince = models.CharField(max_length=255)
    ValidThrough = models.CharField(max_length=255)
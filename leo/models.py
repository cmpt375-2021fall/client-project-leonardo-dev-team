from django.db import models

# Create your models here.

class Calendar(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.title


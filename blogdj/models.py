from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titel = models.CharField(max_length=100)
    body = models.CharField(max_length=3000)
    image =models.URLField()
    author = models.ForeignKey(User)
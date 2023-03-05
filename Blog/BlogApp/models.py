from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return self.title
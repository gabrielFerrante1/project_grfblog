from django.db import models
from blogs.models import Blog
from accounts.models import User

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Dislike(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)


class Like(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)


class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300) 
    date = models.DateTimeField(auto_now_add=True, blank=True)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)

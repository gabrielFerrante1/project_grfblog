from django.db import models
from accounts.models import User 


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    color_primary = models.CharField(max_length=30)
    color_secondary = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Warning(models.Model):
    title = models.TextField()
    txtcolor = models.CharField(max_length=30)
    bgcolor = models.CharField(max_length=30)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Area(models.Model):
    name = models.CharField(max_length=120)

class Visible_Area(models.Model):
    visible = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

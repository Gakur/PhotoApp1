from django.db import models
from django.db.models.manager import Manager

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    imagecaption = models.TextField()
    profile = models.ForeignKey(pk= id)
    likes = models.CharField(max_length=30)
    comments = models.CharField(max_length=150)

class Profile(models.Model):
    profilephoto = models.ImageField()
    bio = models.CharField(max_length=200)
        

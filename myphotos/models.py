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

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()   

    def update_caption(self, newcaption):
        self.imagecaption = newcaption  

    @classmethod
    def get_images_by_user(cls,id):
        sent_pics = Image.objects.filter(user_id=id)
        return sent_pics

    @classmethod
    def get_images_by_id(cls,id):
        fetched_pic = Image.objects.get(id = id)
        return  fetched_pic

    def __str__(self):
    	return self.user.username

    def save_profile(self):
    	self.save()
       

class Profile(models.Model):
    profilephoto = models.ImageField()
    bio = models.TextField(max_length=200)
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)


    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    @classmethod 
    def search_profile(cls,search_term):
        got_profiles = cls.objects.filter(first_name__icontains = search_term)
        return got_profiles
        

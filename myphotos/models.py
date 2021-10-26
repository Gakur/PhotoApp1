from django.db import models
# from django.db.models.manager import Manager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    imagecaption = models.TextField(max_length=250, blank=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
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


class Profile(models.Model):
    profilephoto = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)


    
    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	pic = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='comment')
	comment= models.TextField( blank=True)
	
	def __str__(self):
		return self.comment


	def save_comment(self):
		self.save()

	def delete_comment(self):
		self.delete()

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'        


class Likes(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __int__(self):
		return self.user    

	def unlike(self):
		self.delete()

	def save_like(self):
		self.save() 	
from django.test import TestCase
from .models import Image, Profile, Comment , Follow, Likes 
from django.contrib.auth.models import User

# Create your tests here.
class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='peter', user=User(username='peter'))
        self.profile_test.save()

        self.image_test = Image(image='default.png', name='test', caption='default test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)

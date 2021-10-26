from django import forms
from .models import Image, Profile, Comment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'profilephoto', 'bio']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'imagecaption')


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)

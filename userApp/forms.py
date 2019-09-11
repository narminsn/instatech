from django import  forms
from .models import  MyUser
from . import  models

class LoginForm(forms.Form):
    email = forms.CharField(label= 'Email',widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class SettingsForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = [
            'full_name', 'username', 'email','headline', 'location','description'
        ]


class Shotadd(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = [
            'title', 'background_image', 'description'
        ]

class Comment(forms.ModelForm):
    class Meta:
        model = models.CommentModel
        fields = ['content']
        # labels = ["Leave a comment..."]

class Profile_image(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['profile_image']


class SocialForm(forms.ModelForm):
    class Meta:
        model = models.UserIcon
        fields = ['website', 'facebook', 'twitter']

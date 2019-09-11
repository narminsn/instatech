from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

from theShots.models import MyUser
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class PostModel(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='posts')
    title = models.CharField(max_length=255,null=True,blank=True)
    preview_count = models.IntegerField(null=True,blank=True)
    like_count = models.IntegerField(null=True,blank=True, default=0)
    comment_count = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    publish_date =models.DateTimeField(auto_now_add=True)
    background_image = models.ImageField(upload_to='posts', null=True,blank=True)

    def __str__(self):
        return self.title


class ImageModel(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE, null=True,blank=True)
    image = models.ImageField(upload_to='posts')
    image_token = models.CharField(max_length=255, null=True, blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def __str__(self):
        return self.post.title

class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    type = models.BooleanField(default=False, null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} => {self.post}'

class FollowModel(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'from {self.from_user} to {self.to_user}'

class UserIcon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=225, null=True, blank=True)
    facebook = models.CharField(max_length=225, null=True, blank=True)
    twitter = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.user.username
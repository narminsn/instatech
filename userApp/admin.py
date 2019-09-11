from django.contrib import admin
from userApp import models
# Register your models here.


admin.site.register(models.PostModel)

admin.site.register(models.ImageModel)

admin.site.register(models.LikeModel)

admin.site.register(models.CommentModel)

admin.site.register(models.FollowModel)

admin.site.register(models.UserIcon)
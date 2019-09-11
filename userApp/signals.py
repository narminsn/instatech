# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.contrib.auth import get_user_model
# from .models import ProfileModel
# User = get_user_model()
#
#
#
# @receiver(post_save, sender=User, dispatch_uid='crate_profile')
# def create_profile(*args,**kwargs):
#     obj = kwargs.get("instance")
#     created = kwargs.get("created")
#     if created:
#         ProfileModel.objects.create(
#             user = obj
#         )
#
#

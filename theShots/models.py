from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, UserManager
import random
import  string
from django.utils import timezone
from django.conf import settings
# User = get_user_model()
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import  get_user_model

# User = get_user_model()

# from django.contrib.auth import

# Create your models here.
#
# class Register(AbstractUser):
#     email = models.EmailField(unique=True)

USER_MODEL =settings.AUTH_USER_MODEL


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=True, blank=True,   unique=True)
    first_name = models.CharField(_('Name'),  null=False, max_length=255, blank=False)
    last_name = models.CharField(_('Last Name'), null=False, max_length=255, blank=False)
    full_name = models.CharField(_('Full Name'), null=True, max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=False)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    telephone = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile', null=True,blank=True)
    location = models.CharField(max_length=255, null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    headline = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    check = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    is_superuser = models.BooleanField(_("superuser"), default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    # is_anonymous = False
    is_authenticated = True

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_image(self):
        if self.profile_image:
            return self.profile_image.url

        else:
            return 'https://forwardsummit.ca/wp-content/uploads/2019/01/avatar-default.png'

    def __str__(self):
        return "{}".format(self.username)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        # unique_together = ("username", "email")

User = MyUser()


class MenuModel(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name


class CopyrightModel(models.Model):
    text = RichTextField()



class IconsModel(models.Model):
    icon = models.CharField(max_length=255)
    url = models.CharField(max_length=455)
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class FooterText(models.Model):
    name = models.CharField(max_length=255)
    text = RichTextField(null=True,blank=True)
    button_text = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class FooterUrls(models.Model):
    text = models.ForeignKey('FooterText', on_delete=models.CASCADE, null=True,blank=True)
    # name = models.CharField(max_length=255,null=True,blank=True)
    url_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.text.name

class HeaderModel(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    text = models.TextField()
    background_image = models.ImageField(upload_to='header', null=True, blank=True)
    color = models.CharField(null=True, blank=True, max_length=255)
    form_text = models.CharField(null=True, blank=True, max_length=455)
    logo = models.ImageField(upload_to='header', null=True,blank=True)

    statistics_background = models.ImageField(upload_to='statistics', null=True, blank=True)
    statistics_color = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return  self.title

class StaffPick(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    text = models.TextField()
    button_text = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.subtitle


class OfferModel(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.subtitle

class Offersection(models.Model):
    model =  models.ForeignKey('OfferModel', on_delete=models.CASCADE)
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
         return self.title

class StaticticsModel(models.Model):
    icon = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "statistics"

def generate_token(size=120, chars=string.ascii_letters + string.digits):
    return  "".join(random.choice(chars) for i in range(size))

class VerificationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=120, default=generate_token)
    expire_date = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.token}"




class AboutModel(models.Model):
    title = models.CharField(max_length=255, null=True,blank=True)
    subtitle = models.CharField(max_length=255, null=True,blank=True)
    subtext = models.CharField(max_length=455,null=True,blank=True)
    text = RichTextField()


class AboutTeam(models.Model):
    title = models.CharField(max_length=345, null=True, blank=True)
    subtitle = models.CharField(max_length=245, null=True,blank=True)
    text = models.TextField(null=True,blank=True)

class TeamModel(models.Model):
    model = models.ForeignKey(AboutTeam, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True,blank=True)
    mission = models.CharField(max_length=255)
    about = models.TextField()
    image = models.ImageField(upload_to='team/', null=True,blank=True)

class TeamIcon(models.Model):
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)
    icon = models.CharField(max_length=255)
    url = models.CharField(max_length=455)



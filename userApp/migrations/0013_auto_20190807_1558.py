# Generated by Django 2.2.3 on 2019-08-07 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userApp', '0012_profilemodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='name',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]

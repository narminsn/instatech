# Generated by Django 2.2.3 on 2019-08-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_remove_profilemodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]

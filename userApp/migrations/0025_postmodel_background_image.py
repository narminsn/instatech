# Generated by Django 2.2.3 on 2019-08-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0024_auto_20190813_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]

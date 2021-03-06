# Generated by Django 2.2.3 on 2019-08-13 13:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theShots', '0006_auto_20190809_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('subtext', models.CharField(blank=True, max_length=455, null=True)),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=345, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=245, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theShots.AboutTeam')),
            ],
        ),
        migrations.CreateModel(
            name='TeamIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=455)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theShots.TeamModel')),
            ],
        ),
    ]

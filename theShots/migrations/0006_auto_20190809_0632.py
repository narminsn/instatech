# Generated by Django 2.2.3 on 2019-08-09 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theShots', '0005_auto_20190809_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='about',
            new_name='headline',
        ),
    ]

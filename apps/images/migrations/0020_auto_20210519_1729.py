# Generated by Django 3.1.9 on 2021-05-19 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0019_auto_20210519_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='computations',
            new_name='cache',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='computations',
            new_name='cache',
        ),
    ]

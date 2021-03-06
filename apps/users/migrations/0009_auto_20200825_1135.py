# Generated by Django 3.0.7 on 2020-08-25 11:35

import functools

from django.db import migrations, models

import core.fields.file_field


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200822_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=functools.partial(
                    core.fields.file_field._generate_upload_path,
                    *(),
                    **{'path': 'users/avatars'}
                ),
            ),
        ),
    ]

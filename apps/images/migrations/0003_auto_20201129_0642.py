# Generated by Django 3.1.3 on 2020-11-29 06:42

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20201129_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='image',
            name='key',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, unique=True, verbose_name='key'
            ),
        ),
        migrations.AlterField(
            model_name='video',
            name='key',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, unique=True, verbose_name='key'
            ),
        ),
    ]

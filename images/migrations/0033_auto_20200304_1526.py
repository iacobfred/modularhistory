# Generated by Django 3.0.2 on 2020-03-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0032_auto_20200224_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='embed_code',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

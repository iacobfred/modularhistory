# Generated by Django 3.0.2 on 2020-02-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0101_auto_20200209_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='title2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='documentary',
            name='title2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='title2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='piece',
            name='title2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='speech',
            name='title2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

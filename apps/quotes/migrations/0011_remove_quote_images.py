# Generated by Django 3.1.11 on 2021-06-03 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0010_auto_20210603_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='images',
        ),
    ]
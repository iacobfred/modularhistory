# Generated by Django 3.0.4 on 2020-03-04 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0033_auto_20200304_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='length',
            new_name='duration',
        ),
    ]

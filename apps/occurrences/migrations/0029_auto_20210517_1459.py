# Generated by Django 3.1.9 on 2021-05-17 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0028_auto_20210517_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newoccurrence',
            name='related_quotes',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='related_quotes',
        ),
    ]
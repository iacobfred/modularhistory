# Generated by Django 3.0.2 on 2020-02-09 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0104_auto_20200209_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='speech',
            name='venue',
        ),
    ]

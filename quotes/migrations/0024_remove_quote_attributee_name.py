# Generated by Django 3.0.2 on 2020-02-01 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0023_auto_20200201_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='attributee_name',
        ),
    ]

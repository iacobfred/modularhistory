# Generated by Django 3.1.11 on 2021-05-29 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propositions', '0018_auto_20210529_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typedproposition',
            name='old_locations',
        ),
    ]
# Generated by Django 3.1.9 on 2021-05-08 23:30

import concurrency.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0019_auto_20210512_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='version',
            field=concurrency.fields.IntegerVersionField(
                default=0, help_text='record revision number'
            ),
        ),
    ]

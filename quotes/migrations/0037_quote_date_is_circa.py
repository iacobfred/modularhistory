# Generated by Django 3.0.2 on 2020-02-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0036_auto_20200216_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='date_is_circa',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

# Generated by Django 3.1.11 on 2021-05-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0007_auto_20210528_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='date_string',
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name='date string'
            ),
        ),
    ]

# Generated by Django 3.1.12 on 2021-06-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0004_auto_20210624_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceattribution',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='sourcecontainment',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]

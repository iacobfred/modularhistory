# Generated by Django 3.1.4 on 2020-12-03 21:28

from django.db import migrations

from apps.dates.fields import HistoricDateTimeField


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0010_auto_20201201_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='date',
            field=HistoricDateTimeField(blank=True, null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='end_date',
            field=HistoricDateTimeField(blank=True, null=True, verbose_name='end date'),
        ),
    ]

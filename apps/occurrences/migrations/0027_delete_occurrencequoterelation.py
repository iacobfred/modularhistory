# Generated by Django 3.1.9 on 2021-05-16 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0026_auto_20210516_1649'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OccurrenceQuoteRelation',
        ),
    ]

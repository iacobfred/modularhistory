# Generated by Django 3.0.2 on 2020-02-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0059_occurrence_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='hidden',
            field=models.BooleanField(blank=True, default=False, help_text="Don't let this item appear in search results."),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='verified',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

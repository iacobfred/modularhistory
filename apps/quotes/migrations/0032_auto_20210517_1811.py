# Generated by Django 3.1.9 on 2021-05-17 18:11

from django.db import migrations

import apps.sources.models.model_with_sources


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0013_auto_20210517_1459'),
        ('quotes', '0031_auto_20210517_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='sources',
            field=apps.sources.models.model_with_sources.SourcesField(
                blank=True,
                related_name='quotes',
                through='quotes.Citation',
                to='sources.Source',
                verbose_name='sources',
            ),
        ),
    ]

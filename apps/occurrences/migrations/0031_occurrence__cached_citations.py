# Generated by Django 3.1.9 on 2021-05-18 17:19

from django.db import migrations

import core.fields.json_field


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0030_occurrence_cached_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='_cached_citations',
            field=core.fields.json_field.JSONField(default=list, editable=False),
        ),
    ]

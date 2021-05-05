# Generated by Django 3.1.3 on 2020-11-29 21:22

from django.db import migrations

import core.fields
import core.fields.html_field
from apps.dates.fields import HistoricDateTimeField


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0008_auto_20201129_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='date',
            field=HistoricDateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='description',
            field=core.fields.HTMLField(
                default='...',
                paragraphed=True,
                processor=core.fields.html_field.process,
                verbose_name='Description',
            ),
            preserve_default=False,
        ),
    ]

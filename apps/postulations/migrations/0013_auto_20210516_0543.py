# Generated by Django 3.1.9 on 2021-05-16 05:43

from django.db import migrations, models

import core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0009_source_new_tags'),
        ('postulations', '0012_auto_20210515_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulation',
            name='new_citations',
        ),
        migrations.AddField(
            model_name='postulation',
            name='sources',
            field=models.ManyToManyField(
                blank=True,
                related_name='postulation_citations',
                to='sources.Source',
                verbose_name='sources',
            ),
        ),
        migrations.AlterField(
            model_name='postulation',
            name='notes',
            field=core.fields.HTMLField(
                blank=True,
                null=True,
                paragraphed=True,
                processed=False,
                processor=None,
                verbose_name='note',
            ),
        ),
    ]
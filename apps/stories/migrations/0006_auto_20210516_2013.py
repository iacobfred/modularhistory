# Generated by Django 3.1.9 on 2021-05-16 20:13

import django.db.models.deletion
from django.db import migrations, models

import core.fields.json_field


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0010_auto_20210516_0543'),
        ('stories', '0005_auto_20210516_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryCitation',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'position',
                    models.PositiveSmallIntegerField(blank=True, default=0, null=True),
                ),
                (
                    'citation_phrase',
                    models.CharField(
                        blank=True,
                        choices=[
                            (None, ''),
                            ('quoted in', 'quoted in'),
                            ('cited in', 'cited in'),
                            ('partially reproduced in', 'partially reproduced in'),
                        ],
                        default=None,
                        max_length=25,
                        null=True,
                    ),
                ),
                ('pages', core.fields.json_field.JSONField(default=list)),
                (
                    'proposition',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='stories.story'
                    ),
                ),
                (
                    'source',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='storycitation_citations',
                        to='sources.source',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='story',
            name='sources',
            field=models.ManyToManyField(
                blank=True,
                related_name='story_citations',
                through='stories.StoryCitation',
                to='sources.Source',
                verbose_name='sources',
            ),
        ),
    ]

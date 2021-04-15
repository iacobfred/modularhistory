# Generated by Django 3.1.3 on 2020-11-27 23:23

import uuid

import django.db.models.deletion
import gm2m.fields
from django.db import migrations, models

import core.fields
import core.fields.historic_datetime_field
import core.fields.html_field
import core.fields.json_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('images', '0001_initial'),
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
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
                    'computations',
                    core.fields.json_field.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                ('date_is_circa', models.BooleanField(blank=True, default=False)),
                (
                    'verified',
                    models.BooleanField(default=False, verbose_name='verified'),
                ),
                (
                    'key',
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    'hidden',
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text="Don't let this item appear in search results.",
                    ),
                ),
                (
                    'text',
                    core.fields.HTMLField(
                        paragraphed=True,
                        processor=core.fields.html_field.process,
                        verbose_name='Text',
                    ),
                ),
                (
                    'bite',
                    core.fields.HTMLField(
                        blank=True,
                        null=True,
                        paragraphed=None,
                        processor=core.fields.html_field.process,
                        verbose_name='Bite',
                    ),
                ),
                (
                    'pretext',
                    core.fields.HTMLField(
                        blank=True,
                        help_text='Content to be displayed before the quote',
                        null=True,
                        paragraphed=False,
                        processor=core.fields.html_field.process,
                        verbose_name='Pretext',
                    ),
                ),
                (
                    'context',
                    core.fields.HTMLField(
                        blank=True,
                        help_text='Content to be displayed after the quote',
                        null=True,
                        paragraphed=True,
                        processor=core.fields.html_field.process,
                        verbose_name='Context',
                    ),
                ),
                (
                    'date',
                    core.fields.historic_datetime_field.HistoricDateTimeField(
                        null=True
                    ),
                ),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='QuoteRelation',
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
                ('object_id', models.PositiveIntegerField()),
                (
                    'position',
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text='Determines the order of quotes.',
                        null=True,
                    ),
                ),
                (
                    'content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='contenttypes.contenttype',
                    ),
                ),
                (
                    'quote',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='relations',
                        to='quotes.quote',
                    ),
                ),
            ],
            options={
                'ordering': ['position', 'quote'],
                'unique_together': {('quote', 'content_type', 'object_id', 'position')},
            },
        ),
        migrations.CreateModel(
            name='QuoteImage',
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
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text='Set to 0 if the image is positioned manually.',
                        null=True,
                    ),
                ),
                (
                    'image',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to='images.image'
                    ),
                ),
                (
                    'quote',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='image_relations',
                        to='quotes.quote',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuoteBite',
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
                ('start', models.PositiveIntegerField()),
                ('end', models.PositiveIntegerField()),
                (
                    'quote',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='bites',
                        to='quotes.quote',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuoteAttribution',
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
                ('position', models.PositiveSmallIntegerField(blank=True, default=0)),
                (
                    'attributee',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='quote_attributions',
                        to='entities.entity',
                    ),
                ),
                (
                    'quote',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='attributions',
                        to='quotes.quote',
                    ),
                ),
            ],
            options={
                'ordering': ['position'],
                'unique_together': {('quote', 'attributee')},
            },
        ),
        migrations.AddField(
            model_name='quote',
            name='attributees',
            field=models.ManyToManyField(
                blank=True,
                related_name='quotes',
                through='quotes.QuoteAttribution',
                to='entities.Entity',
            ),
        ),
        migrations.AddField(
            model_name='quote',
            name='images',
            field=models.ManyToManyField(
                blank=True,
                related_name='quotes',
                through='quotes.QuoteImage',
                to='images.Image',
            ),
        ),
        migrations.AddField(
            model_name='quote',
            name='related',
            field=gm2m.fields.GM2MField(
                'occurrences.Occurrence',
                'entities.Entity',
                'quotes.Quote',
                blank=True,
                related_name='related_quotes',
                through='quotes.QuoteRelation',
                through_fields=['quote', 'content_object', 'content_type', 'object_id'],
            ),
        ),
        migrations.AlterUniqueTogether(
            name='quote',
            unique_together={('date', 'bite')},
        ),
    ]

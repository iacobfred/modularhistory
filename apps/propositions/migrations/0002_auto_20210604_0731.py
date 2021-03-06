# Generated by Django 3.1.12 on 2021-06-04 07:21

import django.db.models.deletion
from django.db import migrations, models

import apps.images.models.model_with_images
import apps.places.models.model_with_locations
import apps.quotes.models.model_with_related_quotes
import core.fields.m2m_foreign_key


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        ('propositions', '0001_initial'),
        ('entities', '0002_auto_20210604_0731'),
        ('quotes', '0001_initial'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoterelation',
            name='quote',
            field=core.fields.m2m_foreign_key.ManyToManyForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='propositions_quoterelation_set',
                to='quotes.quote',
            ),
        ),
        migrations.AddField(
            model_name='proposition',
            name='images',
            field=apps.images.models.model_with_images.ImagesField(
                blank=True,
                related_name='proposition_set',
                through='propositions.ImageRelation',
                to='images.Image',
                verbose_name='images',
            ),
        ),
        migrations.AddField(
            model_name='proposition',
            name='locations',
            field=apps.places.models.model_with_locations.LocationsField(
                blank=True,
                related_name='proposition_set',
                through='propositions.Location',
                to='places.Place',
                verbose_name='related quotes',
            ),
        ),
        migrations.AddField(
            model_name='proposition',
            name='related_entities',
            field=models.ManyToManyField(
                blank=True,
                related_name='proposition_set',
                to='entities.Entity',
                verbose_name='related entities',
            ),
        ),
        migrations.AddField(
            model_name='proposition',
            name='related_quotes',
            field=apps.quotes.models.model_with_related_quotes.RelatedQuotesField(
                blank=True,
                related_name='propositions',
                through='propositions.QuoteRelation',
                to='quotes.Quote',
                verbose_name='related quotes',
            ),
        ),
    ]

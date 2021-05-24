# Generated by Django 3.1.11 on 2021-05-21 05:54

from django.db import migrations

import apps.quotes.models.model_with_related_quotes
import apps.sources.models.model_with_sources


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_remove_quote_version'),
        ('sources', '0001_initial'),
        ('propositions', '0005_auto_20210521_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typedproposition',
            name='related_quotes',
            field=apps.quotes.models.model_with_related_quotes.RelatedQuotesField(
                blank=True,
                related_name='propositions',
                through='propositions.QuoteRelation',
                to='quotes.Quote',
                verbose_name='related quotes',
            ),
        ),
        migrations.AlterField(
            model_name='typedproposition',
            name='sources',
            field=apps.sources.models.model_with_sources.SourcesField(
                blank=True,
                related_name='propositions',
                through='propositions.Citation',
                to='sources.Source',
                verbose_name='sources',
            ),
        ),
    ]
# Generated by Django 3.1.12 on 2021-06-04 07:21

import django.db.models.deletion
from django.db import migrations, models

import core.fields.m2m_foreign_key


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entities', '0001_initial'),
        ('images', '0001_initial'),
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoterelation',
            name='quote',
            field=core.fields.m2m_foreign_key.ManyToManyForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='entities_quoterelation_set',
                to='quotes.quote',
            ),
        ),
        migrations.AddField(
            model_name='imagerelation',
            name='content_object',
            field=core.fields.m2m_foreign_key.ManyToManyForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='_image_relations',
                to='entities.entity',
                verbose_name='entity',
            ),
        ),
        migrations.AddField(
            model_name='imagerelation',
            name='image',
            field=core.fields.m2m_foreign_key.ManyToManyForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='_entities_imagerelation_set',
                to='images.image',
            ),
        ),
        migrations.AddField(
            model_name='idea',
            name='promoters',
            field=models.ManyToManyField(
                blank=True, related_name='ideas', to='entities.Entity'
            ),
        ),
        migrations.AddField(
            model_name='entityimage',
            name='entity',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='image_relations',
                to='entities.entity',
            ),
        ),
        migrations.AddField(
            model_name='entityimage',
            name='image',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='entity_relations',
                to='images.image',
            ),
        ),
        migrations.AddField(
            model_name='entityidea',
            name='entity',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='entity_ideas',
                to='entities.entity',
                verbose_name='entity',
            ),
        ),
        migrations.AddField(
            model_name='entityidea',
            name='idea',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='entity_ideas',
                to='entities.idea',
                verbose_name='idea',
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='affiliated_entities',
            field=models.ManyToManyField(
                blank=True,
                related_name='_entity_affiliated_entities_+',
                through='entities.Affiliation',
                to='entities.Entity',
            ),
        ),
    ]

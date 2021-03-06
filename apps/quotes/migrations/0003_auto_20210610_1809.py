# Generated by Django 3.1.12 on 2021-06-10 18:09

import django.db.models.deletion
from django.db import migrations

import core.fields.m2m_foreign_key


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('quotes', '0002_auto_20210604_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerelation',
            name='content_object',
            field=core.fields.m2m_foreign_key.ManyToManyForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='image_relations',
                to='quotes.quote',
                verbose_name='quote',
            ),
        ),
        migrations.AlterField(
            model_name='imagerelation',
            name='image',
            field=core.fields.m2m_foreign_key.ManyToManyForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='quotes_imagerelation_set',
                to='images.image',
            ),
        ),
        migrations.DeleteModel(
            name='QuoteImage',
        ),
    ]

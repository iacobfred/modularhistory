# Generated by Django 3.1.12 on 2021-06-27 22:07

import django.db.models.deletion
from django.db import migrations, models

import core.fields.m2m_foreign_key


class Migration(migrations.Migration):

    dependencies = [
        ('propositions', '0012_auto_20210627_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiseGroupInclusion',
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
                    'premise',
                    core.fields.m2m_foreign_key.ManyToManyForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='propositions_premisegroupinclusion_relations',
                        to='propositions.proposition',
                    ),
                ),
                (
                    'premise_group',
                    core.fields.m2m_foreign_key.ManyToManyForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='propositions_premisegroupinclusion_relations',
                        to='propositions.premisegroup',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='premisegroup',
            name='premises',
            field=models.ManyToManyField(
                through='propositions.PremiseGroupInclusion',
                to='propositions.Proposition',
                verbose_name='premises',
            ),
        ),
    ]

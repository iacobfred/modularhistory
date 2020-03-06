# Generated by Django 3.0.1 on 2020-01-24 14:54

from django.db import migrations
import history.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0018_person_affiliations'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='birth_datetime',
            field=history.fields.historic_datetime_field.HistoricDateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='death_datetime',
            field=history.fields.historic_datetime_field.HistoricDateTimeField(blank=True, null=True),
        ),
    ]

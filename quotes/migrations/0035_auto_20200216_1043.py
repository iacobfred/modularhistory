# Generated by Django 3.0.2 on 2020-02-16 10:43

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    for quote in apps.get_model('quotes', 'Quote').objects.all():
        quote.key = uuid.uuid4()
        quote.save(update_fields=['key'])


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0034_quote_key'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]

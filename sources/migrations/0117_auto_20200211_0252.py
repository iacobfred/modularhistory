# Generated by Django 3.0.2 on 2020-02-11 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0116_remove_source_editors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='editors2',
            new_name='editors',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='editors2',
            new_name='editors',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='editors2',
            new_name='editors',
        ),
        migrations.RenameField(
            model_name='journalentry',
            old_name='editors2',
            new_name='editors',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='editors2',
            new_name='editors',
        ),
        migrations.RenameField(
            model_name='piece',
            old_name='editors2',
            new_name='editors',
        ),
    ]

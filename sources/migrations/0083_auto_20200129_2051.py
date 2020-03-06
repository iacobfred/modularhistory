# Generated by Django 3.0.1 on 2020-01-29 20:51

from django.db import migrations
import history.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0082_auto_20200129_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='file_page_offset',
        ),
        migrations.RemoveField(
            model_name='book',
            name='file_page_offset',
        ),
        migrations.RemoveField(
            model_name='document',
            name='file_page_offset',
        ),
        migrations.RemoveField(
            model_name='essay',
            name='file_page_offset',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='file_page_offset',
        ),
        migrations.AlterField(
            model_name='publicationnumber',
            name='file',
            field=history.fields.file_field.SourceFileField(blank=True, null=True, upload_to='sources/'),
        ),
        migrations.AlterField(
            model_name='publicationvolume',
            name='file',
            field=history.fields.file_field.SourceFileField(blank=True, null=True, upload_to='sources/'),
        ),
    ]

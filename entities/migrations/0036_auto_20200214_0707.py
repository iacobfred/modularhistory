# Generated by Django 3.0.2 on 2020-02-14 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0035_classification_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classification',
            options={'ordering': ['name']},
        ),
    ]

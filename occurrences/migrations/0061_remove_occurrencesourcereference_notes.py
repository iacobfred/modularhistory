# Generated by Django 3.0.2 on 2020-02-25 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0060_auto_20200224_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occurrencesourcereference',
            name='notes',
        ),
    ]

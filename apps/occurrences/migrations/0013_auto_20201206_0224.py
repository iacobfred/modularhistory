# Generated by Django 3.1.4 on 2020-12-06 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0012_auto_20201203_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occurrenceimage',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='occurrenceimage',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='occurrencequoterelation',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0038_auto_20200201_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='years_before_present',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-02 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0023_auto_20200202_0152'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='entityimage',
            unique_together=set(),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0122_auto_20200211_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcefile',
            name='name2',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]

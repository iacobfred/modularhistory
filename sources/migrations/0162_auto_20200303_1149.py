# Generated by Django 3.0.2 on 2020-03-03 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0161_auto_20200301_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='journal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sources.Journal'),
        ),
    ]

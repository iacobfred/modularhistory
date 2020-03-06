# Generated by Django 3.0.2 on 2020-02-10 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0107_auto_20200209_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='repository_name',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='repository_name',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='repository_name',
        ),
        migrations.AlterField(
            model_name='collection',
            name='repository',
            field=models.ForeignKey(help_text='the collecting institution', on_delete=django.db.models.deletion.CASCADE, to='sources.Repository'),
        ),
    ]

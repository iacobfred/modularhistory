# Generated by Django 3.1.9 on 2021-05-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20210428_2009'),
        ('postulations', '0015_postulation_sources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulation',
            name='new_tags',
            field=models.ManyToManyField(
                blank=True,
                related_name='postulation_set',
                to='topics.Topic',
                verbose_name='tags',
            ),
        ),
    ]
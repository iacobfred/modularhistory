# Generated by Django 3.0.2 on 2020-02-02 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0018_image_description'),
        ('entities', '0024_auto_20200202_0154'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='entityimage',
            unique_together={('entity', 'image')},
        ),
    ]

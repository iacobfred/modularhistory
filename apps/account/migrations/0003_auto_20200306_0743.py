# Generated by Django 3.0.4 on 2020-03-06 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200306_0712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
    ]
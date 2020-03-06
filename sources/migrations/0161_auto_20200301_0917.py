# Generated by Django 3.0.2 on 2020-03-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0160_affidavit_certifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speech',
            name='type2',
            field=models.CharField(choices=[('address', 'address'), ('discourse', 'discourse'), ('lecture', 'lecture'), ('sermon', 'sermon'), ('speech', 'speech'), ('statement', 'statement')], default='speech', max_length=10),
        ),
    ]

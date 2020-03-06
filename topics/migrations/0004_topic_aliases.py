# Generated by Django 3.0.1 on 2019-12-29 17:21

from django.db import migrations, models
import history.fields


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20191229_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='aliases',
            field=history.fields.array_field.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None),
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-31 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0016_auto_20200131_1208'),
        ('occurrences', '0030_auto_20200131_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='occurrences', to='occurrences.Year'),
        ),
        migrations.AlterField(
            model_name='occurrenceimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Image'),
        ),
        migrations.AlterField(
            model_name='occurrenceimage',
            name='occurrence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='occurrences.Occurrence'),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-10 12:08

from django.db import migrations, models
import django.db.models.deletion
import history.fields.array_field
import history.fields.historic_datetime_field
import history.fields.html_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', history.fields.historic_datetime_field.HistoricDateField(blank=True, null=True)),
                ('end_date', history.fields.historic_datetime_field.HistoricDateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('aliases', history.fields.array_field.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='entities.Classification')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('entities.person', 'person'), ('entities.deity', 'deity'), ('entities.group', 'group'), ('entities.organization', 'organization')], db_index=True, max_length=255)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('aliases', history.fields.array_field.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('birth_date', history.fields.historic_datetime_field.HistoricDateTimeField(blank=True, null=True)),
                ('death_date', history.fields.historic_datetime_field.HistoricDateTimeField(blank=True, null=True)),
                ('description', history.fields.html_field.HTMLField(blank=True, null=True)),
                ('affiliated_entities', models.ManyToManyField(blank=True, related_name='_entity_affiliated_entities_+', through='entities.Affiliation', to='entities.Entity')),
            ],
            options={
                'verbose_name_plural': 'Entities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', history.fields.html_field.HTMLField(blank=True, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='entities.Entity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleFulfillment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', history.fields.historic_datetime_field.HistoricDateField(blank=True, null=True)),
                ('end_date', history.fields.historic_datetime_field.HistoricDateField(blank=True, null=True)),
                ('affiliation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_fulfillments', to='entities.Affiliation')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fulfillments', to='entities.Role')),
            ],
            options={
                'unique_together': {('affiliation', 'role', 'start_date')},
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', history.fields.html_field.HTMLField(blank=True, null=True)),
                ('promoters', models.ManyToManyField(blank=True, related_name='ideas', to='entities.Entity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_images', to='entities.Entity')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_entities', to='images.Image')),
            ],
            options={
                'unique_together': {('entity', 'image')},
            },
        ),
        migrations.CreateModel(
            name='EntityClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_classifications', to='entities.Classification')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_classifications', to='entities.Entity')),
            ],
            options={
                'unique_together': {('entity', 'classification')},
            },
        ),
        migrations.AddField(
            model_name='entity',
            name='classifications',
            field=models.ManyToManyField(blank=True, related_name='entities', through='entities.EntityClassification', to='entities.Classification'),
        ),
        migrations.AddField(
            model_name='entity',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='entities', through='entities.EntityImage', to='images.Image'),
        ),
        migrations.AddField(
            model_name='entity',
            name='parent_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_organizations', to='entities.Entity'),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='affiliated_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Entity'),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affiliations', to='entities.Entity'),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='affiliations', through='entities.RoleFulfillment', to='entities.Role'),
        ),
        migrations.CreateModel(
            name='Deity',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Deities',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.entity',),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.entity',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Organizations',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.entity',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
            ],
            options={
                'verbose_name_plural': 'People',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.entity',),
        ),
        migrations.CreateModel(
            name='EntityIdea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_ideas', to='entities.Entity')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_ideas', to='entities.Idea')),
            ],
            options={
                'unique_together': {('entity', 'idea')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='affiliation',
            unique_together={('entity', 'affiliated_entity', 'start_date')},
        ),
    ]

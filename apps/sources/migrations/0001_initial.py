# Generated by Django 3.1.3 on 2020-11-27 23:23

import functools
import uuid

import django.db.models.deletion
import gm2m.fields
from django.db import migrations, models

import core.fields
import core.fields.file_field
import core.fields.historic_datetime_field
import core.fields.html_field
import core.fields.json_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('places', '0001_initial'),
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'computations',
                    core.fields.json_field.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                (
                    'citation_phrase',
                    models.CharField(
                        blank=True,
                        choices=[
                            (None, ''),
                            ('quoted in', 'quoted in'),
                            ('cited in', 'cited in'),
                            ('partially reproduced in', 'partially reproduced in'),
                        ],
                        default=None,
                        max_length=25,
                        null=True,
                    ),
                ),
                ('object_id', models.PositiveIntegerField()),
                (
                    'position',
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text='Determines the order of references.',
                        null=True,
                    ),
                ),
                (
                    'content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='contenttypes.contenttype',
                    ),
                ),
            ],
            options={
                'ordering': ['position', 'source'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'computations',
                    core.fields.json_field.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        blank=True,
                        help_text='e.g., "Adam S. Bennion papers"',
                        max_length=100,
                        null=True,
                    ),
                ),
                ('url', models.URLField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'type',
                    models.CharField(
                        choices=[
                            ('sources.journal', 'journal'),
                            ('sources.magazine', 'magazine'),
                            ('sources.newspaper', 'newspaper'),
                        ],
                        db_index=True,
                        max_length=255,
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ('aliases', models.CharField(blank=True, max_length=100, null=True)),
                (
                    'description',
                    core.fields.HTMLField(
                        blank=True,
                        null=True,
                        paragraphed=True,
                        processor=core.fields.html_field.process,
                    ),
                ),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'type',
                    models.CharField(
                        choices=[
                            ('sources.textualsource', 'textual source'),
                            (
                                'sources.sourcewithpagenumbers',
                                'source with page numbers',
                            ),
                            ('sources.piece', 'piece'),
                            ('sources.essay', 'essay'),
                            ('sources.documentsource', 'document source'),
                            ('sources.document', 'document'),
                            ('sources.affidavit', 'affidavit'),
                            ('sources.article', 'article'),
                            ('sources.book', 'book'),
                            ('sources.sectionsource', 'section source'),
                            ('sources.section', 'section'),
                            ('sources.chapter', 'chapter'),
                            ('sources.correspondence', 'correspondence'),
                            ('sources.email', 'email'),
                            ('sources.letter', 'letter'),
                            ('sources.memorandum', 'memorandum'),
                            ('sources.spokensource', 'spoken source'),
                            ('sources.speech', 'speech'),
                            ('sources.address', 'address'),
                            ('sources.discourse', 'discourse'),
                            ('sources.lecture', 'lecture'),
                            ('sources.sermon', 'sermon'),
                            ('sources.statement', 'statement'),
                            ('sources.interview', 'interview'),
                            ('sources.journalentry', 'journal entry'),
                            ('sources.videosource', 'video source'),
                            ('sources.documentary', 'documentary'),
                            ('sources.webpage', 'web page'),
                        ],
                        db_index=True,
                        max_length=255,
                    ),
                ),
                (
                    'computations',
                    core.fields.json_field.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                ('date_is_circa', models.BooleanField(blank=True, default=False)),
                (
                    'verified',
                    models.BooleanField(default=False, verbose_name='verified'),
                ),
                (
                    'key',
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    'hidden',
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text="Don't let this item appear in search results.",
                    ),
                ),
                (
                    'full_string',
                    models.CharField(
                        blank=True,
                        max_length=500,
                        unique=True,
                        verbose_name='searchable string',
                    ),
                ),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                (
                    'url',
                    models.URLField(
                        blank=True,
                        help_text='URL where the source can be accessed online',
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    'description',
                    core.fields.HTMLField(
                        blank=True,
                        null=True,
                        paragraphed=True,
                        processor=core.fields.html_field.process,
                    ),
                ),
                (
                    'date',
                    core.fields.historic_datetime_field.HistoricDateTimeField(
                        blank=True, null=True
                    ),
                ),
                (
                    'publication_date',
                    core.fields.historic_datetime_field.HistoricDateTimeField(
                        blank=True, null=True
                    ),
                ),
                ('creators', models.CharField(blank=True, max_length=100, null=True)),
                (
                    'extra',
                    core.fields.json_field.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                (
                    'original_publication_date',
                    core.fields.historic_datetime_field.HistoricDateTimeField(
                        blank=True, null=True
                    ),
                ),
            ],
            options={
                'ordering': ['creators', '-date'],
            },
        ),
        migrations.CreateModel(
            name='SourceFile',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'file',
                    core.fields.file_field.SourceFileField(
                        blank=True,
                        null=True,
                        unique=True,
                        upload_to=functools.partial(
                            core.fields.file_field._generate_upload_path,
                            *(),
                            **{'path': 'sources/'}
                        ),
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    'page_offset',
                    models.SmallIntegerField(
                        blank=True,
                        default=0,
                        help_text='The difference between the page numbers displayed on the pages and the actual page numbers of the electronic file (a positive number if the electronic page number is greater than the textualpage number; a negative number if the textual page number is greater than the electronic page number).',
                    ),
                ),
                (
                    'first_page_number',
                    models.SmallIntegerField(
                        blank=True,
                        default=1,
                        help_text='The page number that is visibly displayed on the page on which the relevant text begins (usually 1).',
                    ),
                ),
                ('uploaded_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SourceContainment',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'page_number',
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                (
                    'end_page_number',
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True)),
                (
                    'phrase',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('', '-----'),
                            ('archived', 'archived'),
                            ('cited', 'cited'),
                            ('copy', 'copy'),
                            ('quoted', 'quoted'),
                            ('recorded', 'recorded'),
                            ('reproduced', 'reproduced'),
                            ('transcribed', 'transcribed'),
                        ],
                        default='',
                        max_length=12,
                    ),
                ),
                (
                    'container',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='container_containments',
                        to='sources.source',
                    ),
                ),
                (
                    'source',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='source_containments',
                        to='sources.source',
                    ),
                ),
            ],
            options={
                'ordering': ['position', 'source'],
            },
        ),
        migrations.CreateModel(
            name='SourceAttribution',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True)),
                (
                    'attributee',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='source_attributions',
                        to='entities.entity',
                    ),
                ),
                (
                    'source',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='attributions',
                        to='sources.source',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='source',
            name='attributees',
            field=models.ManyToManyField(
                blank=True,
                related_name='attributed_sources',
                through='sources.SourceAttribution',
                to='entities.Entity',
            ),
        ),
        migrations.AddField(
            model_name='source',
            name='collection',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='documents',
                to='sources.collection',
            ),
        ),
        migrations.AddField(
            model_name='source',
            name='containers',
            field=models.ManyToManyField(
                blank=True,
                related_name='contained_sources',
                through='sources.SourceContainment',
                to='sources.Source',
            ),
        ),
        migrations.AddField(
            model_name='source',
            name='db_file',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='sources',
                to='sources.sourcefile',
                verbose_name='file',
            ),
        ),
        migrations.AddField(
            model_name='source',
            name='location',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='places.place',
            ),
        ),
        migrations.AddField(
            model_name='source',
            name='original_edition',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='subsequent_editions',
                to='sources.source',
            ),
        ),
        migrations.AddField(
            model_name='source',
            name='publication',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='sources.publication',
            ),
        ),
        migrations.AddField(
            model_name='source',
            name='related',
            field=gm2m.fields.GM2MField(
                'quotes.Quote',
                'occurrences.Occurrence',
                blank=True,
                related_name='sources',
                through='sources.Citation',
                through_fields=[
                    'source',
                    'content_object',
                    'content_type',
                    'object_id',
                ],
            ),
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'computations',
                    core.fields.json_field.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        blank=True,
                        help_text='e.g., "L. Tom Perry Special Collections"',
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    'owner',
                    models.CharField(
                        blank=True,
                        help_text='e.g., "Harold B. Lee Library, Brigham Young University"',
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    'location',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='repositories',
                        to='places.place',
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'Repositories',
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='repository',
            field=models.ForeignKey(
                help_text='the collecting institution',
                on_delete=django.db.models.deletion.CASCADE,
                to='sources.repository',
            ),
        ),
        migrations.AddField(
            model_name='citation',
            name='source',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='citations',
                to='sources.source',
            ),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.publication',),
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.publication',),
        ),
        migrations.CreateModel(
            name='Newspaper',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.publication',),
        ),
        migrations.CreateModel(
            name='SpokenSource',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.source',),
        ),
        migrations.CreateModel(
            name='TextualSource',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.source',),
        ),
        migrations.CreateModel(
            name='VideoSource',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.source',),
        ),
        migrations.CreateModel(
            name='PageRange',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('page_number', models.PositiveSmallIntegerField()),
                (
                    'end_page_number',
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                (
                    'citation',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='pages',
                        to='sources.citation',
                    ),
                ),
            ],
            options={
                'ordering': ['page_number'],
                'unique_together': {('citation', 'page_number')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together={('name', 'repository')},
        ),
        migrations.AlterUniqueTogether(
            name='citation',
            unique_together={('source', 'content_type', 'object_id', 'position')},
        ),
        migrations.CreateModel(
            name='Address',
            fields=[],
            options={
                'verbose_name_plural': 'Addresses',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.spokensource',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.textualsource',),
        ),
        migrations.CreateModel(
            name='Discourse',
            fields=[],
            options={
                'verbose_name_plural': 'Discourses',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.spokensource',),
        ),
        migrations.CreateModel(
            name='Documentary',
            fields=[],
            options={
                'verbose_name_plural': 'Documentaries',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.videosource',),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.spokensource',),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[],
            options={
                'verbose_name_plural': 'Lectures',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.spokensource',),
        ),
        migrations.CreateModel(
            name='SectionSource',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.textualsource',),
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[],
            options={
                'verbose_name_plural': 'Sermons',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.spokensource',),
        ),
        migrations.CreateModel(
            name='SourceWithPageNumbers',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.textualsource',),
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[],
            options={
                'verbose_name_plural': 'Speeches',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.spokensource',),
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[],
            options={
                'verbose_name_plural': 'Statements',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.spokensource',),
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.textualsource',),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.sourcewithpagenumbers',),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.sectionsource',),
        ),
        migrations.CreateModel(
            name='DocumentSource',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.sourcewithpagenumbers',),
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[],
            options={
                'verbose_name_plural': 'Journal entries',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.sourcewithpagenumbers',),
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.sourcewithpagenumbers',),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.sectionsource',),
        ),
        migrations.CreateModel(
            name='Affidavit',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.documentsource',),
        ),
        migrations.CreateModel(
            name='Correspondence',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.documentsource',),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.documentsource',),
        ),
        migrations.CreateModel(
            name='Essay',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.piece',),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.correspondence',),
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.correspondence',),
        ),
        migrations.CreateModel(
            name='Memorandum',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.correspondence',),
        ),
    ]

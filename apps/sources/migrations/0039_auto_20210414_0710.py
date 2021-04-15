# Generated by Django 3.1.8 on 2021-04-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0038_auto_20210414_0608'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Affidavit',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
        migrations.DeleteModel(
            name='Correspondence',
        ),
        migrations.DeleteModel(
            name='Discourse',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Documentary',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Essay',
        ),
        migrations.DeleteModel(
            name='Interview',
        ),
        migrations.DeleteModel(
            name='JournalEntry',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.DeleteModel(
            name='Letter',
        ),
        migrations.DeleteModel(
            name='Memorandum',
        ),
        migrations.DeleteModel(
            name='Piece',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='SectionSource',
        ),
        migrations.DeleteModel(
            name='Sermon',
        ),
        migrations.DeleteModel(
            name='Speech',
        ),
        migrations.DeleteModel(
            name='SpokenSource',
        ),
        migrations.DeleteModel(
            name='Statement',
        ),
        migrations.DeleteModel(
            name='VideoSource',
        ),
        migrations.DeleteModel(
            name='WebPage',
        ),
        migrations.AlterField(
            model_name='source',
            name='type',
            field=models.CharField(
                choices=[
                    ('sources.textualsource', 'textual source'),
                    ('sources.sourcewithpagenumbers', 'source with page numbers'),
                    ('sources.documentsource', 'document source'),
                ],
                db_index=True,
                max_length=255,
            ),
        ),
    ]
from typing import Optional

from django.db import models
from django.db.models import ForeignKey, CASCADE, SET_NULL
from django.utils.safestring import SafeText, mark_safe
from django.core.exceptions import ValidationError

from history.fields.file_field import SourceFileField
from history.fields.html_field import HTMLField
from history.models import Model
from .base import TitleMixin, TextualSource, SourceFile, _Piece


class DocumentMixin(Model):
    collection = ForeignKey('Collection', related_name='%(class)s', null=True, blank=True, on_delete=CASCADE)
    collection_number = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text='aka acquisition number'
    )
    location_info = models.CharField(
        max_length=400, null=True, blank=True,
        help_text='Ex: John H. Alexander Papers, Series 1: Correspondence, 1831-1848, Folder 1'
    )

    HISTORICAL_ITEM_TYPE = 'writing'

    class Meta:
        abstract = True


class _Document(DocumentMixin, TextualSource):
    collection = ForeignKey('Collection', related_name='%(class)s', null=True, blank=True, on_delete=CASCADE)
    collection_number = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text='aka acquisition number'
    )
    location_info = models.CharField(
        max_length=400, null=True, blank=True,
        help_text='Ex: John H. Alexander Papers, Series 1: Correspondence, 1831-1848, Folder 1'
    )

    HISTORICAL_ITEM_TYPE = 'writing'

    class Meta:
        abstract = True


class Collection(Model):
    name = models.CharField(max_length=100, help_text='e.g., "Adam S. Bennion papers"', null=True, blank=True)
    repository = ForeignKey('Repository', on_delete=CASCADE, help_text='the collecting institution')
    link = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ['name', 'repository']

    def __str__(self):
        string = ''
        if self.name:
            string += f'{self.name}' if self.name else ''
            string += ', ' if self.repository else ''
        string += f'{self.repository}' if self.repository else ''
        return string


class Repository(Model):
    name = models.CharField(max_length=100, null=True, blank=True,
                            help_text='e.g., "L. Tom Perry Special Collections"')
    location = models.CharField(max_length=100, null=True, blank=True,
                                help_text='e.g., "Harold B. Lee Library, Brigham Young University"')

    class Meta:
        verbose_name_plural = 'Repositories'

    def __str__(self):
        return f'{self.name}, {self.location}'


class Document(TitleMixin, _Document):
    def __str__(self) -> SafeText:
        string = ''
        string += f'{self.creators}, ' if self.creators else ''
        string += f'"{self.title}," ' if self.title else ''
        string += f'{self.date.string}, ' if self.date else ''
        string += f'archived in {self.collection}' if self.collection else ''
        return mark_safe(string)


letter_types = (
    ('email', 'email'),
    ('letter', 'letter'),
    ('memorandum', 'memorandum'),
)


class Letter(_Document):
    recipient = models.CharField(max_length=100, null=True, blank=True)
    type2 = models.CharField(max_length=10, choices=letter_types, default='letter')

    class Meta:
        verbose_name = 'correspondence'
        verbose_name_plural = 'correspondence'

    def __str__(self) -> SafeText:
        string = f'{self.creators}, letter to {self.recipient or "<Unknown>"}'
        if self.date:
            string += ', dated ' if self.date.day_is_known else ', '
            string += self.date.string
        if self.collection:
            string += f', archived in {self.collection}'
        # elif self.container:
        #     containment = self.source_containments.get(container=self.container)
        #     string += f', '
        #     string += f'{containment.phrase} ' or ''
        #     string += f'in {self.container}'
        return mark_safe(string)


class Affidavit(_Document):
    certifier = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        string = f'{self.creators or self.attributees.first()}, '
        string += f'affidavit sworn {self.date_html} at {self.location} before {self.certifier}'
        return mark_safe(string)

    def clean(self):
        super().clean()
        if not self.location:
            raise ValidationError('Affidavit needs a certification location.')


class JournalEntry(_Piece):

    class Meta:
        verbose_name_plural = 'Journal entries'

    def __str__(self) -> SafeText:
        string = f'{self.creators}, journal ' if self.creators else 'Journal '
        string += f'entry dated {self.date.string}' if self.date else ''
        return mark_safe(string)

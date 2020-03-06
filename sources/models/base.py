import re
from os import listdir, rename
from os.path import isfile, join
from typing import Optional, Tuple

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import ForeignKey, ManyToManyField, CASCADE, SET_NULL
from django.utils.safestring import SafeText, mark_safe

from history import settings
from history.fields.file_field import SourceFileField, upload_to
from history.fields.historic_datetime_field import HistoricDateTimeField, HistoricDateField
from history.fields.html_field import HTMLField
from history.models import Model, PolymorphicModel, DatedModel, SearchableMixin
# from places.models import Venue
from ..manager import Manager


class SourceFile(Model):
    file = SourceFileField(upload_to=upload_to('sources/'), null=True, blank=True)
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    page_offset = models.SmallIntegerField(default=0, blank=True)
    first_page_number = models.SmallIntegerField(default=1, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.file_name} (page offset: {self.page_offset})'

    @property
    def file_name(self) -> Optional[str]:
        if self.file:
            return self.file.name.replace('sources/', '')
        return None

    @property
    def url(self) -> str:
        return self.file.url

    def full_clean(self, exclude=None, validate_unique=True):
        super().full_clean(exclude=exclude, validate_unique=validate_unique)
        if not self.file:
            raise ValidationError('No file.')

    def save(self, *args, **kwargs):
        if self.name and self.name != self.file_name:
            full_path = f'{settings.MEDIA_ROOT}/sources'
            files = [f for f in listdir(full_path) if isfile(join(full_path, f))]
            if self.file_name in files:
                rename(f'{full_path}/{self.file_name}', f'{full_path}/{self.name}')
                self.file.name = f'sources/{self.name}'
        if 'sources/sources' in self.file.name:
            raise ValidationError(f'Bad file name: {self.file.name}')
        if self.file.name.endswith('None'):
            raise ValidationError(f'Bad file name: {self.file.name}')
        super().save(*args, **kwargs)
        # Set the name attr after the initial save,
        # because the initial save modifies the file name.
        if not self.name:
            self.name = self.file_name
            super().save()


class Source(PolymorphicModel, DatedModel, SearchableMixin):
    """A source for quotes or historical information."""
    objects: Manager = Manager()

    db_string = models.CharField(verbose_name='database string', max_length=500, blank=True, unique=True)
    attributees = ManyToManyField('entities.Entity', through='SourceAttribution', related_name='attributed_sources')
    creators = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    date = HistoricDateTimeField(null=True, blank=True)
    publication_date = HistoricDateField(null=True, blank=True)
    containers = ManyToManyField('self', through='SourceContainment', symmetrical=False,
                                 through_fields=('source', 'container'), related_name='contained_sources', blank=True)
    location = ForeignKey('places.Place', related_name='publications', on_delete=SET_NULL, null=True, blank=True)
    file = ForeignKey(SourceFile, related_name='sources', on_delete=SET_NULL, null=True, blank=True)

    HISTORICAL_ITEM_TYPE = 'publication'

    searchable_fields = ['db_string', 'description']

    class Meta:
        ordering = ['creators', '-date']

    def __str__(self):
        return str(self.object)

    @property
    def admin_file_link(self) -> SafeText:
        element = ''
        if self.get_file():
            element = f'<a class="btn display-source" href="{self.object.file_url}" target="_blank">file</a>'
        return mark_safe(element)

    @property
    def container(self) -> Optional['Source']:
        if not self.containment:
            return None
        return self.containment.container

    @property
    def containment(self) -> Optional['SourceContainment']:
        if not self.source_containments.exists():
            return None
        return self.source_containments.order_by('position')[0]

    @property
    def html(self) -> SafeText:
        html = self.string
        if self.file_url:
            html += (
                f'<a href="{self.file_url}" class="mx-1 display-source"'
                f' data-toggle="modal" data-target="#modal">'
                f'<i class="fas fa-search"></i>'
                f'</a>'
            )
        elif self.link:
            link = self.link
            if self.page_number and 'www.sacred-texts.com' in link:
                link += f'#page_{self.page_number}'
            html += (
                f'<a href="{link}" class="mx-1" target="_blank">'
                f'<i class="fas fa-search"></i>'
                f'</a>'
            )
        return html

    @property
    def object(self) -> 'Source':
        """Return the object with the correct content type."""
        try:
            ct = ContentType.objects.get(id=self.polymorphic_ctype_id)
            return ct.model_class().objects.get(id=self.id)
        except Exception as e:
            print(f'EXCEPTION: Trying to get child object for {self} resulted in: {e}')
            return self

    @property
    def string(self) -> SafeText:
        if hasattr(self.object, 'string_override'):
            return mark_safe(self.object.string_override)
        string = str(self)
        if self.source_containments.exists():
            containments = self.source_containments.order_by('position')[:2]
            container_strings = []
            same_creator = True
            for c in containments:
                if c.container.creators != self.creators:
                    same_creator = False
                container_string = str(c.container)
                if same_creator and self.creators and self.creators in container_string:
                    container_string = container_string[len(f'{self.creators}, '):]
                container_string = (f'{c.phrase} in {container_string}' if c.phrase
                                    else f'in {container_string}')
                container_strings.append(container_string)
            containers = ', and '.join(container_strings)
            string += f', {containers}'
        return mark_safe(string)

    @property
    def file_url(self) -> Optional[str]:
        file = self.get_file()
        return file.url if file else None

    def get_file(self) -> Optional[SourceFile]:
        return self.file if self.file else self.container.get_file() if self.container else None

    def natural_key(self) -> Tuple:
        return self.db_string,

    def clean(self):
        pass
        # # Create related historical occurrence
        # if not Episode.objects.filter(type=self.HISTORICAL_ITEM_TYPE).exists():
        #     Episode.objects.create(
        #         type=self.HISTORICAL_ITEM_TYPE,
        #     )

    def save(self, *args, **kwargs):
        self.full_clean()
        self.db_string = self.string
        super().save(*args, **kwargs)


class TitleMixin(Model):
    title = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        abstract = True


containment_phrases = (
    ('', '-----'),
    ('archived', 'archived'),
    ('cited', 'cited'),
    ('copy', 'copy'),
    ('quoted', 'quoted'),
    ('recorded', 'recorded'),
    ('reproduced', 'reproduced'),
    ('transcribed', 'transcribed')
)


class SourceContainment(Model):
    source = ForeignKey(Source, on_delete=CASCADE, related_name='source_containments')
    container = ForeignKey(Source, on_delete=CASCADE, related_name='container_containments')
    page_number = models.PositiveSmallIntegerField(null=True, blank=True)
    end_page_number = models.PositiveSmallIntegerField(null=True, blank=True)
    position = models.PositiveSmallIntegerField(default=1)
    phrase = models.CharField(max_length=12, choices=containment_phrases, default='', blank=True)

    class Meta:
        ordering = ['position', 'source']

    def __str__(self):
        return mark_safe(f'{self.phrase} in {self.container}')


class TextualSource(Source):
    editors = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def file_page_number(self) -> Optional[int]:
        file = self.get_file()
        if file:
            if self.containment and self.containment.page_number:
                return self.containment.page_number + file.page_offset
            return file.first_page_number + file.page_offset
        return None

    @property
    def file_url(self) -> Optional[str]:
        file_url = super().file_url
        if file_url and self.file_page_number:
            file_url += f'#page={self.file_page_number}'
        return file_url


class _Piece(TextualSource):
    page_number = models.PositiveSmallIntegerField(null=True, blank=True)
    end_page_number = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def string(self) -> SafeText:
        string = super().string
        # Fix placement of commas after double-quoted titles
        string = string.replace('," ,', ',"')
        string = string.replace('",', ',"')
        return mark_safe(string)

    @property
    def file_page_number(self) -> Optional[int]:
        file = self.get_file()
        if file:
            if self.page_number:
                return self.page_number + file.page_offset
            elif self.container:
                containment = self.source_containments.get(container=self.container)
                if containment.page_number:
                    return containment.page_number + file.page_offset
        return None


class SourceAttribution(Model):
    """An entity (e.g., a writer or organization) to which a source is attributed."""
    source = ForeignKey(Source, on_delete=CASCADE)
    attributee = ForeignKey('entities.Entity', on_delete=CASCADE, related_name='source_attributions')
    position = models.PositiveSmallIntegerField(default=1, blank=True)


source_types = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('T', 'Tertiary')
)


class SourceReference(Model):
    """Abstract base class for a reference to a source."""
    source: Source
    position = models.PositiveSmallIntegerField(verbose_name='reference position', default=1, blank=True)
    page_number = models.PositiveSmallIntegerField(null=True, blank=True)
    end_page_number = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self) -> SafeText:
        page_string = ''
        if self.page_number:
            page_string = f'p{"p" if self.end_page_number else ""}. {self.page_number}'
            if self.end_page_number:
                page_string += f'–{self.end_page_number}'
        return mark_safe(f'{self.source.string}{", " if page_string else ""}{page_string}')

    @property
    def html(self) -> SafeText:
        html = str(self)
        if self.source_file_url:
            html += (
                f'<a href="{self.source_file_url}" class="mx-2 display-source"'
                f' data-toggle="modal" data-target="#modal">'
                f'<i class="fas fa-search"></i>'
                f'</a>'
            )
        elif self.source.link:
            link = self.source.link
            if self.page_number and 'www.sacred-texts.com' in link:
                link += f'#page_{self.page_number}'
            html += (
                f'<a href="{link}" class="mx-2" target="_blank">'
                f'<i class="fas fa-search"></i>'
                f'</a>'
            )
        return mark_safe(html)

    @property
    def source_file_page_number(self) -> Optional[int]:
        file = self.source.get_file()
        if file:
            if self.page_number:
                return self.page_number + file.page_offset
            elif hasattr(self.source, 'file_page_number'):
                print(f'>>>> {self.source} >>>>>>> {self.source.file_page_number}')
                return self.source.file_page_number
        return None

    @property
    def source_file_url(self) -> Optional[str]:
        file_url = self.source.file_url
        if file_url and self.source_file_page_number:
            if 'page=' in file_url:
                file_url = re.sub(r'page=\d+', f'page={self.source_file_page_number}', file_url)
            else:
                file_url = file_url + f'#page={self.source_file_page_number}'
        return file_url

    def clean(self):
        if self.end_page_number and self.end_page_number < self.page_number:
            raise ValidationError('The end page number must be greater than the start page number.')


class SourceFactDerivation(SourceReference):
    source = ForeignKey(Source, related_name='fact_derivations', on_delete=CASCADE)
    fact = ForeignKey('topics.Fact', related_name='fact_derivations', on_delete=CASCADE)

from django.db import models
from django.utils.html import format_html

from modularhistory.models import Model

IMPORTANCE_OPTIONS = (
    (1, 'Primary'),
    (2, 'Secondary'),
    (3, 'Tertiary'),
    (4, 'Quaternary'),
    (5, 'Quinary'),
    (6, 'Senary'),
    (7, 'Septenary'),
)


class OccurrenceLocation(Model):
    """A place being a site of an occurrence."""

    occurrence = models.ForeignKey('occurrences.Occurrence', on_delete=models.CASCADE)
    location = models.ForeignKey(
        'places.Place', related_name='location_occurrences', on_delete=models.CASCADE
    )
    importance = models.IntegerField(choices=IMPORTANCE_OPTIONS, default=1)

    class Meta:
        unique_together = ['occurrence', 'location']

    def __str__(self):
        """Return the string representation of the occurrence–location association."""
        return f'{self.location} : {self.occurrence}'


class OccurrenceQuoteRelation(Model):
    """An involvement of an entity in an occurrence."""

    occurrence = models.ForeignKey(
        'occurrences.Occurrence',
        related_name='occurrence_quote_relations',
        on_delete=models.CASCADE,
    )
    quote = models.ForeignKey(
        'quotes.Quote',
        related_name='quote_occurrence_relations',
        on_delete=models.CASCADE,
    )
    position = models.PositiveSmallIntegerField(
        null=True, blank=True
    )  # TODO: add cleaning logic

    class Meta:
        unique_together = ['occurrence', 'quote']
        ordering = ['position', 'quote']

    def __str__(self) -> str:
        """Return the string representation of the occurrence quote relation."""
        return format_html(f'{self.quote.citation}')

    @property
    def quote_pk(self) -> str:
        """TODO: write docstring."""
        return self.quote.pk


class OccurrenceEntityInvolvement(Model):
    """An involvement of an entity in an occurrence."""

    occurrence = models.ForeignKey('occurrences.Occurrence', on_delete=models.CASCADE)
    entity = models.ForeignKey(
        'entities.Entity',
        related_name='occurrence_involvements',
        on_delete=models.CASCADE,
    )
    importance = models.PositiveSmallIntegerField(choices=IMPORTANCE_OPTIONS, default=1)

    class Meta:
        unique_together = ['occurrence', 'entity']

    def __str__(self) -> str:
        """Return the string representation of the occurrence entity involvement."""
        return format_html(f'{self.occurrence.date_string}: {self.occurrence.summary}')
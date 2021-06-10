from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.fields.html_field import HTMLField
from core.models.positioned_relation import PositionedRelation


class FallacyIdentification(PositionedRelation):
    """An identification of a fallacy."""


class Fallacy(models.Model):
    """A fallacy."""

    name = models.CharField(max_length=40)
    description = HTMLField(
        verbose_name=_('description'),
        paragraphed=True,
        processed=False,
        blank=True,
    )

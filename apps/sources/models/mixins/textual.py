from typing import Optional

from django.db import models

from modularhistory.fields import HistoricDateTimeField


class TextualMixin(models.Model):
    """Mixin model for textual sources."""

    editors = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    original_edition = models.ForeignKey(
        to='self',
        related_name='subsequent_editions',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    original_publication_date = HistoricDateTimeField(null=True, blank=True)

    class Meta:
        """Meta options for the _Engagement model."""

        # https://docs.djangoproject.com/en/3.1/ref/models/options/#model-meta-options.
        abstract = True

    @property
    def file_page_number(self) -> Optional[int]:
        """Return the page number to which the source file should be opened."""
        file = self.source_file
        if file:
            if self.containment and self.containment.page_number:
                return self.containment.page_number + file.page_offset
            return file.first_page_number + file.page_offset
        return None

    @property
    def source_file_url(self) -> Optional[str]:
        """Return the URL to be used to open the source file."""
        file_url = super().source_file_url
        if file_url and self.file_page_number:
            file_url = f'{file_url}#page={self.file_page_number}'
        return file_url

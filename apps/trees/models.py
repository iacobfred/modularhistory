"""Based on https://github.com/peopledoc/django-ltree-demo."""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.trees.fields import LtreeField
from core.models.model import Model


class TreeModel(Model):
    """Implements Postgres ltree for self-referencing hierarchy."""

    parent = models.ForeignKey(
        to='self',
        null=True,
        # Direct children can be accessed via the `children` property.
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name=_('parent'),
    )
    name = models.TextField(verbose_name=_('name'))
    # The `key` field is a unique identifier for the node.
    # It is derived from the `name` field.
    key = models.CharField(max_length=32, unique=True, null=True)
    # The `path` field represents the path from the root to the node,
    # where each node is represented by its key.
    path = LtreeField()

    class Meta:
        """Meta options for DatedModel."""

        # https://docs.djangoproject.com/en/3.1/ref/models/options/#model-meta-options
        abstract = True

    def save(self, *args, **kwargs):
        """Save the model instance to the database."""
        if not self.key:
            self.set_key()
        return super().save(*args, **kwargs)

    def set_key(self):
        """Set the model instance's key value based on its name."""
        name: str = self.name
        self.key = name.lower().replace(' ', '_')
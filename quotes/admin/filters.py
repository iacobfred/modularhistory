import re

from admin_auto_filters.filters import AutocompleteFilter
from django.contrib.admin import SimpleListFilter
from django.db.models import Count
from django.urls import reverse
from django.utils.safestring import mark_safe

from entities.models import Entity


class AttributeeFilter(AutocompleteFilter):
    """TODO: add docstring."""

    title = 'attributee'
    field_name = 'attributees'

    PARAMETER_NAME = 'attributees__pk__exact'

    def __init__(self, request, params, model, model_admin):
        """TODO: add docstring."""
        super().__init__(request, params, model, model_admin)
        rendered_widget = self.rendered_widget
        if self.value():
            entity = Entity.objects.get(pk=self.value())
            rendered_widget = mark_safe(
                re.sub(r'(selected>).+(</option>)',
                       rf'\g<1>{entity}\g<2>',
                       rendered_widget)
            )
        self.rendered_widget = rendered_widget

    def get_autocomplete_url(self, request, model_admin):
        """TODO: add docstring."""
        return reverse('admin:entity_search')

    def queryset(self, request, queryset):
        """TODO: add docstring."""
        if self.value():
            return queryset.filter(**{self.PARAMETER_NAME: self.value()})
        else:
            return queryset


class AttributeeClassificationFilter(AutocompleteFilter):
    """TODO: add docstring."""

    title = 'attributee classification'
    field_name = 'attributees__classifications'


class HasSourceFilter(SimpleListFilter):
    """TODO: add docstring."""

    title = 'has source'
    parameter_name = 'has_source'

    def lookups(self, request, model_admin):
        """TODO: add docstring."""
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        """TODO: add docstring."""
        if self.value() == 'Yes':
            return queryset.exclude(sources=None)
        if self.value() == 'No':
            return queryset.filter(sources=None)


class AttributeeCountFilter(SimpleListFilter):
    """TODO: add docstring."""

    title = 'attributee count'
    parameter_name = 'attributee_count'

    def lookups(self, request, model_admin):
        """TODO: add docstring."""
        return (
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4+'),
        )

    def queryset(self, request, queryset):
        """TODO: add docstring."""
        queryset = queryset.annotate(attributee_count=Count('attributees'))
        try:
            n = int(self.value())
        except TypeError:  # `All`
            return queryset
        if n == 4:
            return queryset.exclude(attributee_count__lt=n)
        return queryset.filter(attributee_count=n)


class HasMultipleCitationsFilter(SimpleListFilter):
    """TODO: add docstring."""

    title = 'has multiple citations'
    parameter_name = 'has_multiple_citations'

    def lookups(self, request, model_admin):
        """TODO: add docstring."""
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        """TODO: add docstring."""
        queryset = queryset.annotate(citation_count=Count('citations'))
        if self.value() == 'Yes':
            return queryset.exclude(citation_count__lt=2)
        if self.value() == 'No':
            return queryset.filter(citation_count__gte=2)

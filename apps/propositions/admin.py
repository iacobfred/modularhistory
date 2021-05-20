from apps.admin import StackedInline, admin_site
from apps.entities.admin.filters import RelatedEntityFilter
from apps.entities.admin.inlines import AbstractRelatedEntitiesInline
from apps.propositions import models
from apps.search.admin import SearchableModelAdmin
from apps.sources.admin.citations import AbstractSourcesInline
from apps.topics.admin.related_topics import AbstractRelatedTopicsInline
from apps.topics.models.taggable_model import TopicFilter


class RelatedTopicsInline(AbstractRelatedTopicsInline):
    """Inline admin for topic tags."""

    model = models.Proposition.tags.through


class NewRelatedTopicsInline(AbstractRelatedTopicsInline):
    """Inline admin for topic tags."""

    model = models.TypedProposition.tags.through


class SourcesInline(AbstractSourcesInline):
    """Inline admin for sources."""

    model = models.Proposition.sources.through


class NewSourcesInline(AbstractSourcesInline):
    """Inline admin for sources."""

    model = models.TypedProposition.sources.through


class RelatedEntitiesInline(AbstractRelatedEntitiesInline):
    """Inline admin for related entities."""

    model = models.Proposition.related_entities.through


class NewRelatedEntitiesInline(AbstractRelatedEntitiesInline):
    """Inline admin for related entities."""

    model = models.TypedProposition.related_entities.through


class ConclusionsInline(StackedInline):
    """Inline admin for a proposition's supported propositions."""

    verbose_name = 'supported proposition'
    verbose_name_plural = 'supported propositions'
    model = models.Support
    exclude = ['premise', 'conclusion']
    fk_name = 'new_premise'
    autocomplete_fields = ['new_conclusion']
    extra = 0


class PremisesInline(StackedInline):
    """Inline admin for a proposition's premises."""

    verbose_name = 'premise'
    verbose_name_plural = 'premises'
    model = models.Support
    exclude = ['premise', 'conclusion']
    fk_name = 'new_conclusion'
    autocomplete_fields = ['new_premise']
    extra = 0


class AbstractPropositionAdmin(SearchableModelAdmin):
    """Abstract base admin for propositions."""

    exclude = SearchableModelAdmin.exclude + [
        'related_entities',
        'sources',
    ]
    inlines = [
        PremisesInline,
        ConclusionsInline,
        SourcesInline,
        RelatedEntitiesInline,
        RelatedTopicsInline,
    ]
    list_display = [
        'slug',
        'summary',
        'tags_string',
    ]
    list_filter = [
        TopicFilter,
        RelatedEntityFilter,
        'type',
    ]


class TypedPropositionAdmin(AbstractPropositionAdmin):
    model = models.TypedProposition

    exclude = AbstractPropositionAdmin.exclude + ['images', 'locations']
    inlines = [
        PremisesInline,
        ConclusionsInline,
        NewSourcesInline,
        NewRelatedEntitiesInline,
        NewRelatedTopicsInline,
    ]
    list_display = AbstractPropositionAdmin.list_display + ['type']
    search_fields = model.searchable_fields
    list_per_page = 15


admin_site.register(models.TypedProposition, TypedPropositionAdmin)

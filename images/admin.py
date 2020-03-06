from django.contrib.admin import TabularInline

# from taggit_labels.widgets import LabelWidget
# from taggit.forms import TagField
from admin import admin_site, Admin
from entities.models import EntityImage
from occurrences.models import OccurrenceImage
from .models import Image, Video


class EntitiesInline(TabularInline):
    model = EntityImage
    verbose_name = 'entity'
    extra = 1
    autocomplete_fields = ['entity']


class OccurrencesInline(TabularInline):
    model = OccurrenceImage
    verbose_name = 'occurrence'
    extra = 1
    autocomplete_fields = ['occurrence']


class ImageAdmin(Admin):
    list_display = ('admin_image_element', 'caption', 'provider', 'date')
    inlines = [EntitiesInline, OccurrencesInline]
    search_fields = Image.searchable_fields

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        for field_name in ('type',):
            if field_name in fields:
                fields.remove(field_name)
                fields.insert(0, field_name)
        # for field_name in ('position', 'page_number', 'end_page_number', 'notes'):
        #     if field_name in fields:
        #         fields.remove(field_name)
        #         fields.append(field_name)
        return fields


class VideoAdmin(Admin):
    list_display = ['title', 'link']
    search_fields = ['title']
    readonly_fields = ['duration']


admin_site.register(Image, ImageAdmin)
admin_site.register(Video, VideoAdmin)

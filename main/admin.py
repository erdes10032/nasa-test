from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage
from django.utils.html import format_html


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'order')
    list_editable = ('order',)
    ordering = ('order',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" />',
                obj.image.url
            )
        return '—'

    image_preview.short_description = 'Превью'
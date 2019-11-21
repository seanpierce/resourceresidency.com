from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

from .models import Content, Image

admin.site.register(Content)

class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150px" />'.format(obj.image.url))

    def path(self, obj):
        return settings.HOST_NAME + obj.image.url

    image_tag.short_description = 'Preview'

    list_display = ['image_tag',]
    readonly_fields = ['path', 'image_tag']

admin.site.register(Image, ImageAdmin)
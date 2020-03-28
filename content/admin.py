from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

from .models import Content, Event, File

class FileInline(admin.TabularInline):
    model = File

class EventAdmin(admin.ModelAdmin):
    inlines = (FileInline,)

admin.site.register(Content)
admin.site.register(Event, EventAdmin)
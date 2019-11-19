from django.contrib import admin
from .models import Residency

class ResidencyAdmin(admin.ModelAdmin):
    filter_horizontal = ('artists',)

admin.site.register(Residency, ResidencyAdmin)

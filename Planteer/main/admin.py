from django.contrib import admin
from .models import Plant
# Register your models here.

class PlantAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published_at']
    list_filter = ['category', 'published_at', 'is_edible']

admin.site.register(Plant , PlantAdmin)


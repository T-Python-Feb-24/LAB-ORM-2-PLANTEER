from django.contrib import admin
from .models import Plant

class PlantAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'about', 'used_for', 'image', 'category', 'is_edible', 'created_at']
    list_filter = [ 'category', 'is_edible']


admin.site.register(Plant, PlantAdmin)

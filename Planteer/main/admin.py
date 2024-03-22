from django.contrib import admin
from .models import Plant
# Register your models here.


class PlantAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'about', 
        'used_for', 
        'image', 
        'category', 
        'is_edible',
        'created_at'
        ]
    list_filter = [
        'is_edible',
        'category'
    ]

admin.site.register(Plant, PlantAdmin)
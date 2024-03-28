from django.contrib import admin
from .models import Plant, Comment


# Register your models here.

#customizing the admin panel for a Model
class PlantAdmin(admin.ModelAdmin):

    list_display = ['name', 'category', 'used_for', 'created_at']
    list_filter =  ['is_edible', 'category']

admin.site.register(Plant, PlantAdmin)
admin.site.register(Comment)
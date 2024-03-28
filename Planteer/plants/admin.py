from django.contrib import admin
from .models import Plant, Comment
# Register your models here.

class PlantAdmin(admin.ModelAdmin):
    #list to customize the columns
    list_display = ['name', 'category', 'is_edible', 'created_at']
    #adding fliters
    list_filter =  ['is_edible', 'category']

admin.site.register(Plant, PlantAdmin)
admin.site.register(Comment)

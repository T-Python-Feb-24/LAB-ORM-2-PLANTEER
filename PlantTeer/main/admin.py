from django.contrib import admin
from .models import Plant, Comment,Contact

class PlantAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'categroy', 'is_edible','created_at','image','used_for','about']
    
    list_filter =  ['name', 'categroy']

admin.site.register(Plant, PlantAdmin)
admin.site.register(Comment)


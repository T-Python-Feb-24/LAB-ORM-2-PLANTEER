from django.contrib import admin
from .models import Plants
# Register your models here.
class PlantsAdmin(admin.ModelAdmin):
    list_display=['name','category','is_edible','created_at']
    list_filter=['is_edible','category']
admin.site.register(Plants,PlantsAdmin)


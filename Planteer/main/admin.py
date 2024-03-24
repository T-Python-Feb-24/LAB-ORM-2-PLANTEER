from django.contrib import admin
from .models import Plant

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name","created_at","is_edible")

    list_filter =("created_at",)

admin.site.register(Plant,PlantAdmin)

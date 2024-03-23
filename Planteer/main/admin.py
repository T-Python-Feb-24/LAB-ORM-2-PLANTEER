from django.contrib import admin
from .models import Plant

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name","about","used_for","created_at")

    list_filter =("created_at",)

admin.site.register(Plant,PlantAdmin)

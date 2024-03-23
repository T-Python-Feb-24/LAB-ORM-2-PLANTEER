from django.contrib import admin
from .models import Plant
from .models import Contact
# Register your models here.


class PlantAdmin(admin. ModelAdmin):
    list_display = ["name", "created_at", 'is_edible','category']
    list_filter = ['category']
    
admin.site.register(Plant, PlantAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", 'email', 'created_at']
    list_filter = ['created_at']
    
admin.site.register(Contact, ContactAdmin)
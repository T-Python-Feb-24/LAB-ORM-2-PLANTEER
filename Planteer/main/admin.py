from django.contrib import admin
from .models import Plant, Contact
from account.models import Profile


class PlantAdmin(admin.ModelAdmin):

    list_display = ['name', 'image', 'used_for',
                    'category', 'is_edible', 'created_at']

    list_filter = ['is_edible', 'category']


class ContactAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'email']

    list_filter = ['first_name', 'created_at']


admin.site.register(Plant, PlantAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile)

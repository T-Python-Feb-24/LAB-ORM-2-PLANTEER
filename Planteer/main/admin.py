from django.contrib import admin
from .models import Plant, Contact

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display= ('name', 'category', 'is_edible', 'created_at')

    list_filter= ('category', 'is_edible',)

class PublisherCon(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'email', 'created_at')


admin.site.register(Plant, PublisherAdmin)
admin.site.register(Contact, PublisherCon)
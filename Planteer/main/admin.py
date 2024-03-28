from django.contrib import admin
from .models import Plant, Contact, Comment

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display= ('name', 'category', 'is_edible', 'created_at')

    list_filter= ('category', 'is_edible',)

class PublisherCon(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'email', 'created_at')

class PublisherComm(admin.ModelAdmin):
    list_display= ('plant', 'user', 'created_at')

admin.site.register(Plant, PublisherAdmin)
admin.site.register(Contact, PublisherCon)
admin.site.register(Comment, PublisherComm)
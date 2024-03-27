from django.contrib import admin
from .models import Plant , Contact ,Comment 




class PlantAdmin(admin.ModelAdmin):
    #list to customize the columns
    list_display = ['name', 'about', 'used_for', 'is_edible','created_at', 'category']


class ContactAdmin(admin.ModelAdmin):
    #list to customize the columns
    list_display = ['f_name', 'l_name', 'email', 'message','created_at']

class CommentAdmin(admin.ModelAdmin):
    #list to customize the columns
    list_display = ['name', 'content', 'created_at', 'user']

admin.site.register(Plant , PlantAdmin)
admin.site.register(Contact , ContactAdmin)
admin.site.register(Comment , CommentAdmin)
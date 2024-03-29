from django.contrib import admin
from .models import Plant, Comment

# Register your models here.

#customizing the admin panel for a Model
class PostAdmin(admin.ModelAdmin):
    #list to customize the columns
    list_display = ['name', 'category', 'is_edible', 'created_at']
    #adding fliters
    list_filter =  ['name', 'category']

admin.site.register(Plant, PostAdmin)
admin.site.register(Comment)
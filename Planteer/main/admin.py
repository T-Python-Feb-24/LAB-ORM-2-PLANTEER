from django.contrib import admin
from .models import Plant,Comment

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name","created_at","is_edible")

    list_filter =("created_at",)

admin.site.register(Plant,PlantAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=("user", "content" , "plant")
    
admin.site.register(Comment,CommentAdmin)

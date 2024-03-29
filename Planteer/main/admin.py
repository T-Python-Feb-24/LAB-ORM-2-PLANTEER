from django.contrib import admin
from .models import Plant,Comment ,Contact

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name","created_at","is_edible")

    list_filter =("created_at",)

admin.site.register(Plant,PlantAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=("user", "content" , "plant")
    
admin.site.register(Comment,CommentAdmin)

class ContactAdimn(admin.ModelAdmin):
    list_display =("first_name","last_name" ,"email")
     
admin.site.register(Contact,ContactAdimn)
    
from django.contrib import admin
from .models import Plant,Contact, Comment

class PlantAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'about', 'used_for', 'image', 'category', 'is_edible', 'created_at']
    list_filter = [ 'category', 'is_edible']


admin.site.register(Plant, PlantAdmin)

class contact_us(admin.ModelAdmin):
    list_display=["first_name","last_name","email","created_at"]
admin.site.register(Contact,contact_us)


class Comments(admin.ModelAdmin):
    list_display=["full name","content"]

admin.site.register(Comment)
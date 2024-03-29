from django.contrib import admin
from .models import Profile 
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    display_list=("user","about","twitter")

admin.site.register(Profile,ProfileAdmin)
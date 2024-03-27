from django.contrib import admin
from .models import Favorite
# Register your models here.
class favorite(admin.ModelAdmin):
    pass
admin.site.register(Favorite,favorite)
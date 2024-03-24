from django.contrib import admin
from .models import Plant, Contact,Comment
# Register your models here.
class Admin(admin.ModelAdmin):
    list_display=["name",'categore',"about","used_for","is_edible","created_at"]
admin.site.register(Plant, Admin)

class contact_us(admin.ModelAdmin):
    list_display=["first_name","last_name","email","created_at"]
admin.site.register(Contact,contact_us)


class CommentView(admin.ModelAdmin):
    list_display=["Full name","content"]
    
admin.site.register(Comment)

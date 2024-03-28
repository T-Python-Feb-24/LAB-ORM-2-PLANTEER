from django.contrib import admin
from .models import Plant


class Adminmain (admin.ModelAdmin):

   list_display=['name','category','create_at']


admin.site.register(Plant , Adminmain)

'''
admin 
username: abdulah
eamil: A@gmail.com
password: A123456 
------------------
Manger:
UN: Manger
pass: Manger
------------------
staff:
UN: Staff
pass: Staff123
'''
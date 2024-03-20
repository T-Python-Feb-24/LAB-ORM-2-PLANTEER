from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path(""),
    path("plants/all/"),
    path("plants/<plant_id>/detail/"),
    path("plants/search/"),
    path("plants/new/"),
    path("lants/<plant_id>/update/"),
    #Bonus pages :
    path("contact/"),
    path("contact/messages/"),
    
]

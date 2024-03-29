from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("",views.home_page,name="home_page"),
    path("plants/all/",views.all_plants,name="all_plants"),
    path("plants/<plant_id>/detail/",views.plant_detail,name="plant_detail"),
    path("plants/search/",views.search_page,name="search_page"),
    path("plants/new/",views.new_plant,name="new_plant"),
    path("plants/<plant_id>/update/",views.update_plant,name="update_plant"),
    path("plants/<plant_id>/delete/",views.delete_plant,name="delete_plant"),
    path("comments/add/<plant_id>/",views.plant_comment,name="plant_comment"),
    # #Bonus pages :
    path("contact/us/",views.contact_page,name="contact_page"),
    path("contact/messages/",views.contact_messages,name="contact_messages"),

]



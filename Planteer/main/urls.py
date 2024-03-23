from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("",views.home_page,name="home_page"),
    path("plants/all/",views.all_plants,name="all_plants"),
    path("plants/<plant_id>/detail/",views.plant_detail,name="plant_detail"),
    # path("plants/search/"),
    path("plants/new/",views.new_plant,name="new_plant"),
    path("plants/<plant_id>/update/",views.update_plant,name="update_plant"),
    #plant.id = 24 , plant_id =24 
    path("plants/<plant_id>/delete/",views.delete_plant,name="delete_plant"),
    # #Bonus pages :
    # path("contact/"),
    # path("contact/messages/"),

]

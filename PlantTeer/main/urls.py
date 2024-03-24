from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home_page, name="home_page"),
    path("plants/all/", views.all_plants, name="all_plants"),
    path("plants/<plant_id>/detail/", views.detail_plants, name="detail_plants"),
    path("plants/new/", views.add_plants, name="add_plants"),
    path("plants/<plant_id>/update/", views.update_plants, name="update_plants"),
    path("plants/<plant_id>/delete/", views.delete_plants, name="delete_plants"),
    path("plants/search/", views.plants_search, name="plants_search"),

   
]
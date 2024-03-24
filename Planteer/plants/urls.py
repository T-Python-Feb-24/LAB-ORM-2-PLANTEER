from django.urls import path
from . import views

app_name = "plants"

urlpatterns  = [
    path("", views.index_view, name="index_view"),
    path("plants/new/", views.add_plant_view, name="add_plant_view"),
    path("plants/<plant_id>/update/", views.update_plant_view, name="update_plant_view"),
    path("plants/<plant_id>/detail/", views.plant_detail_view, name="plant_detail_view"),
    path("plants/search/", views.plant_search_view, name="plant_search_view"),
    path("plants/all/", views.all_plants_view, name="all_plants_view"),
    path("plants/<plant_id>/delete/", views.delete_plant_view, name="delete_plant_view"),
]


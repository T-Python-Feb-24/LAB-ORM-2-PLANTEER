from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("plant/add/", views.add_plant_view, name="add_plant_view"),
    path("plant/detail/<plant_id>/", views.plant_detail_view, name="plant_detail_view"),
    path("plant/update/<plant_id>/", views.update_plant_view, name="update_plant_view"),
    path("plant/delete/<plant_id>/", views.delete_plant_view, name="delete_plant_view"),
    path("plant/all/", views.all_plant_view, name="all_plant_view"),
    path("plants/search/", views.plants_search_view, name="plant_search_view"),
]
from .import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("plants/all/", views.all_plants, name="all_plants"),
    path("plants/<plant_id>/detail/", views.plant_detail, name="plant_detail"),
    path("plants/new/", views.add_plant, name="add_plant"),
    path("post/update/<post_id>/", views.update_plant, name="update_post_view"),
    path("post/delete/<post_id>/", views.delete_plant, name="delete_post_view"),
    path("plants/search/", views.plant_search, name="plant_search"),
]
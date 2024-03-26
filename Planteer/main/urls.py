from .import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("plants/all/", views.all_plants, name="all_plants"),
    path("plants/<plant_id>/detail/", views.plant_detail, name="plant_detail"),
    path("plants/new/", views.add_plant, name="add_plant"),
    path("plants/update/<plant_id>/", views.update_plant, name="update_plant"),
    path("plants/delete/<plant_id>/", views.delete_plant, name="delete_plant"),
    path("plants/search/", views.plant_search, name="plant_search"),
    # path("contact/", views.contact_us, name="contact_us"),
    path("comments/add/<plant_id>/", views.add_comment, name="add_comment"),
]
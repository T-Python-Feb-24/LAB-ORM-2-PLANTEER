from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("plants/new/", views.add_plant_view, name="add_plant_view"),
    path("plants/<plant_id>/detail/",views.plant_detail_view, name="plant_detail_view"),
    path("plants/<plant_id>/update/", views.update_plant_view, name="update_plant_view"),
    path("plants/<plant_id>/delete/", views.delete_plant_view, name="delete_plant_view"),
    path("plants/all/", views.all_plant_view, name="all_plant_view"),
    path("plants/search/", views.search_view, name="search_view"),
    path("contact/", views.contact_us_view, name="contact_us_view"),
    path("contact/messages/", views.all_messages_view, name="all_messages_view"),
    path("Comments/<plant_id>/add", views.add_comment_view, name="add_comment_view")
]
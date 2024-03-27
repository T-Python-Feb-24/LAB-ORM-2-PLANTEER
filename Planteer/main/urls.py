from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home_view, name="home_view"),
    path("plants/new/", views.add_plants_view, name="add_plants_view"),
    path("plants/all/", views.all_plants_view, name="all_plants_view"),
    path("plants/<plant_id>/detail/", views.detail_view, name="detail_view"),
    path("plants/<plant_id>/update/", views.update_plants_view, name="update_plants_view"),
    path("plant/<plant_id>/delete/", views.delete_plants_view, name="delete_plants_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("contact/messages/", views.message_view, name="message_view"),
    path("plants/search/", views.search_view, name="search_view"),
    path("comments/add/<plant_id>/", views.add_comment_view, name="add_comment_view")

    
   
]

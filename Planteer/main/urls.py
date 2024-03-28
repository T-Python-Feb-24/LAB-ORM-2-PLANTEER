from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.index_view, name="index_view"),
    path('plants/new/', views.new_plant_view, name="new_plant_view"),
    path('plants/search/', views.search_plants_view, name="search_plants_view"),
    path("plants/<plant_id>/detail/",
         views.plant_detail_view, name="plant_detail_view"),
    path("comments/add/<plant_id>/",
         views.add_comment_view, name="add_comment_view"),
    path("plants/<plant_id>/update/",
         views.update_plant_view, name="update_plant_view"),
    path("plants/<plant_id>/delete/",
         views.delete_plant_view, name="delete_plant_view"),
    path("plants/all/", views.all_plants_view, name="all_plants_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("contact/messages/", views.contactUs_messages_view,
         name="contactUs_messages_view"),

]

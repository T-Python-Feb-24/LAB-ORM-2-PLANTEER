from django.urls import path
from . import views

app_name = "main"


urlpatterns  = [
    path("", views.index_view, name="index_view"),
    path("plant/add/", views.add_plant_view, name="add_plant_view"),
    path("plant/detail/<plant_id>/", views.plant_detail_view, name="plant_detail_view"),
    path("plant/update/<plant_id>/", views.update_plant_view, name="update_plant_view"),
    path("plant/delete/<plant_id>/", views.delete_view, name="delete_view"),
    path("plants/all/", views.all_plants_view, name="all_plants_view"),
    path("plants/search/", views.plants_search_view, name="plants_search_view"),
    path("plants/contact/", views.contact_view, name="contact_view"),
    path("contact/messages/",views.messages_view,name="messages_view"),
    path("comment/add/", views.add_comment_view, name="add_comment_view")
]
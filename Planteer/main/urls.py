from django.urls import path
from . import views

app_name="main"

urlpatterns=[
    path('',views.index_page,name='index_page'),
    path('plants/new/',views.add_plants, name="add_plants"),
    path("plants/all/", views.all_plants, name="all_plants"),
    path("plants/details/<plant_id>/",views.plant_detail ,name="plants_details"),
    path("plants/delete/<plant_id>/",views.delete_plant_view ,name="delete_plant_view"),
    path('plants/<plant_id>/update/', views.update_plant_view, name='update_plant_view'),
    path("plants/search/" , views.search_page ,name="search_page"),
    path("contact",views.contact_page ,name="contact_page"),
    path("contact/messages/",views.show_message_page,name="show_message_page"),
]
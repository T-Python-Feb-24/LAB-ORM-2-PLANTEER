
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('plants/add/', views.add_plant, name='add_plant'),
    path("plants/detail/<int:plant_id>/", views.plant_detail, name="plant_detail"),
    path('plants/<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('plants/<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path("plants/all/", views.all_plants_view, name="all_plants_view"),
    path('search/', views.search_plants, name='search_plants'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
     path("comment/<plant_id>/", views.add_comment, name="add_comment")
    
]

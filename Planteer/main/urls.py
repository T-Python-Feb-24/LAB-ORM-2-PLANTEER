from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('plants/new/', views.add_plant, name='add_plant'),
    path('plants/all/', views.all_plant, name='all_plants'),
    path('plants/<plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('plants/<plant_id>/update/', views.update_plant, name='update_plant'),
    path('plants/<plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('plants/search/', views.search, name='search'),
    path('plants/contact_us/', views.contact, name='contact'),
    path('plants/contact_us/messages', views.messages, name='message'),
]
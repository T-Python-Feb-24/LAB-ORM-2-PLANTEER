# from django.urls import path
# from . import views

# app_name = "main"

# urlpatterns  = [
#     path("", views.index_view, name="index_view"),
#     path("post/add/", views.add_post_view, name="add_post_view"),
#     path("post/detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
#     path("post/update/<post_id>/", views.update_post_view, name="update_post_view"),
#     path("post/delete/<post_id>/", views.delete_post_view, name="delete_post_view"),
#     path("post/all/", views.all_posts_view, name="all_posts_view"),
#     path("posts/search/", views.search, name="search")
# ]



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
]

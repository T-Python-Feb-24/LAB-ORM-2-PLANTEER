from django.urls import path
from . import views

app_name  = "favorites"

urlpatterns = [
    path("add/<post_id>/", views.add_remove_favorites_view, name="add_remove_favorites_view"),
    path("user/favorites/", views.user_favorites_view, name="user_favorites_view")
]
from django.urls import path, include
from . import views


app_name  = "user_info"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("user_detail/<username>/", views.user_detail, name="user_detail"), 
    path("profile_update/", views.profile_update, name="profile_update"),   
]
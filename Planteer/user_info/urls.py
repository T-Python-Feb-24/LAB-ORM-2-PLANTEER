from django.urls import path
from . import views

app_name  = "user_info"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("user_detail/<str:username>/", views.user_detail, name="user_detail"), 
    ]
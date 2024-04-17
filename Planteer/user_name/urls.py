from django.urls import path
from . import views

app_name  = "user_name"

urlpatterns = [
    path("register/", views.register_user_view, name="register_user_view"),
    path("login/", views.login_user_view, name="login_user_view"),
    path("logout/", views.logout_user_view, name="logout_user_view"),
    path("profile/<user_name>/", views.user_profile_view, name="user_profile_view"),
    path("update/", views.update_profile_view , name="update_profile_view")


]
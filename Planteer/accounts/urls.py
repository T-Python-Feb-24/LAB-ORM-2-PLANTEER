from django.urls import path
from . import views

app_name  = "accounts"

urlpatterns = [
    path("register/", views.register_user_view, name="register"),
    path("login/", views.login_user_view, name="login"),
    path("logout/", views.logout_user_view, name="logout"),
    path("profile/<user_name>/", views.profile_view, name="profile"),
    path("profile/<user_name>/update", views.update_user, name="update_user"),
]
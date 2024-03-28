from django.urls import path
from . import views

app_name  = "accounts"

urlpatterns = [
    path("register/", views.register_user_view, name="register_user_view"),
    path("login/", views.login_user_view, name="login_user_view"),
    path("logout/", views.logout_user_view, name="logout_user_view"),
    path("userinfo/<user_id>/", views.user_info, name="user_info_view"),
    path("update/profile/<user_id>/", views.update_info, name="update_info"),
]
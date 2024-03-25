from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register_user_view, name="register_user_view"),
    path("login/", views.login_user_view, name="login_user_view"),
    path("logout/", views.logout_user_view, name="logout_user_view"),
    path("detail/<user_id>/", views.user_detail_view, name="user_detail_view")
]
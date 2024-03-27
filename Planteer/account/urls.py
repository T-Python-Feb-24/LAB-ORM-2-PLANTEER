from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("sign_up/", views.sign_up_view, name="sign_up_view"),
    path("user/<user_name>/",
         views.user_profile_view, name="user_profile_view"),
    path("profile/<user_name>/update/",
         views.update_profile_view, name="update_profile_view"),

    path("profiles/", views.profiles_view, name="profiles_view"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
]

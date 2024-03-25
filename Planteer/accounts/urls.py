from django.urls import path
from . import views


app_name="accounts"

urlpatterns=[
    path("register/",views.register_page,name="register_page"),
    path("login/",views.login_page, name="login_page"),
    path("logout/",views.logout_user_view,name="logout_user_view"),
    path("profile/<str:username>/",views.user_profile ,name="user_profile"),
]
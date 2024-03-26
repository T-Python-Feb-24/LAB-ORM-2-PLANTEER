from django.urls import path
from . import views


app_name="accounts"

urlpatterns = [
    path("create/account/", views.create_account,name="create_account" ),
    path("user/login/",views.user_login,name="user_login"),
    path("user/logout/",views.user_logout,name="user_logout"),
    path("user/profile/",views.user_profile,name="user_profile"),
]

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path('user/<str:username>/', views.user_detail, name='user_detail'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

]
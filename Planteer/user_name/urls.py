from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register_user_view, name='register_user_view'),
    path('login/', views.login_user_view, name='login_user_view'),
    path('logout/', views.logout_user_view, name='logout_user_view'),
    path('user/<str:username>/', views.user_detail_view, name='user_detail_view'),
    # Other URL patterns...

]

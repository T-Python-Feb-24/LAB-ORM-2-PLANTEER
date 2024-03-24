from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
   path("",views.home,name="home"),
   path("plants/all/",views.all_plants,name="all_plants_page"),
   path("plants/new/",views.add,name="add_page"),
   path("plants/<plant_id>/detail/",views.detail,name="detail_page"),
   path("plants/<plant_id>/update/",views.update,name="update_page"),
   path("plants/<plant_id>/delete/",views.delete,name="delete_view"),
   path("plants/search/",views.search,name="search_page"),
   path("plants/contact/",views.info,name="contact_page"),
   path("users/message/",views.user_message,name="message_page"),
   path("comments/<plant_id>/" , views.comment , name="comments_view"),

]
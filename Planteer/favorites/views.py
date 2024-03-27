from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Plant
from .models import Favorite
from django.contrib.auth.models import User


# Create your views here.


def add_remove_favorites_view(request: HttpRequest, plant_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user")
    
    try:
        plant = Plant.objects.get(pk=plant_id)


        favored_plant = Favorite.objects.filter(user=request.user, plant=plant).first()

        if not favored_plant:
            favorite = Favorite(user=request.user, plant=plant)
            favorite.save()
        else:
            #delete favorite if already exists
            favored_plant.delete()
    
    except Exception as e:
        print(e)


    return redirect("main:plant_detail", plant_id=plant_id)


def user_favorites_view(request: HttpRequest):

    

    return render(request, "favorites/favorites.html")
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plants,Contact
from datetime import date, timedelta
import math


# Create your views here.

def home_view(request:HttpRequest):
    plants = Plants.objects.all()
    return render(request, "main/home.html", {"plants" : plants })

def add_plants_view(request:HttpRequest):
     
    if request.method == 'POST':
        try:
            new_plant = Plants(
               name=request.POST["name"],
               about=request.POST["about"], 
               used_for=request.POST["used_for"], 
               category=request.POST["category"], 
               is_edible=request.POST.get("is_edible", False), 
               image=request.FILES.get("image", Plants.image.field.default)
               )
            new_plant.save()
            return redirect("main:home_view")
        except Exception as e:
            print(e)

    return render(request, "main/add_plants.html", {"categories" : Plants.categories.choices})
    
def all_plants_view(request:HttpRequest):
     
     if "cat" in request.GET:
      plants = Plants.objects.filter(category=request.GET["cat"])
     else:
      plants = Plants.objects.all()
    
    

    # print(start, end)
     return render(request,"main/all_plants.html", {"plants": plants, "categories": Plants.categories.choices })

def detail_view(request:HttpRequest ,plant_id):
    try:
        #getting a  post detail
        plant = Plants.objects.get(pk=plant_id)
    except Plants.DoesNotExist:
        return render(request)
    except Exception as e:
        print(e)


    return render(request, "main/plants_detail.html", {"plant" : plant})



def update_plants_view(request:HttpRequest, plant_id):

    plant = Plants.objects.get(pk=plant_id)

    if request.method == "POST":
        try:
            plant.name = request.POST["name"]
            plant.about = request.POST["about"]
            plant.used_for = request.POST["used_for"]
            plant.category = request.POST["category"]
            plant.is_edible=request.POST.get("is_edible", False) 
            plant.image = request.FILES.get("image", plant.image)
            plant.save()
            return redirect("main:detail_view", plant_id = plant.id)
        except Exception as e:
            print(e)
    return render(request, 'main/update_plants.html', {"plant" : plant, "categories" : Plants.categories.choices})


def delete_plants_view(request:HttpRequest, plant_id):

    try:
        plant = Plants.objects.get(pk=plant_id)
        plant.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:home_view")

# هنا بارت التواصل والرسائل
def contact_view(request:HttpRequest):
   
   if request.method == 'POST':
        try:
            new_con = Contact(
                first_name=request.POST["first_name"], 
                last_name=request.POST["last_name"], 
                email=request.POST["email"], 
                message= request.POST["message"]
            )
            new_con.save()
            return redirect("main:message_view")
        except Exception as e:
                    print(e)

   return render(request, "main/contact.html")

    
def message_view(request:HttpRequest):
    Contacts = Contact.objects.all()
    return render(request, "main/message.html", {"Contacts" : Contacts })


def search_view(request:HttpRequest):
     plants = []

     if "name" in request.GET:
        plants = Plants.objects.filter(name__contains=request.GET["name"])

     if "category" in request.GET:
        plants = Plants.objects.filter(category__contains=request.GET["category"])

        


     return render(request, "main/plants_search.html", {"plants" : plants})
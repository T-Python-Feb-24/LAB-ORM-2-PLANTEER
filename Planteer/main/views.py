from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from.models import Plant
# Create your views here.

#home page : 
def home_page(request :HttpRequest):
    
# a QuerySet equates to a SELECT statement in sql, You get a QuerySet by using your model’s Manager. Each model has at least one Manager, and it’s called "objects" by default. 
# Basic lookups keyword arguments take the form field__lookuptype=value. 

    plants = Plant.objects.order_by('?').all()[:3]
    
    return render(request,"main/home_page.html",{"plants":plants})

#All Plants page
def all_plants(request :HttpRequest):
    
    plants = Plant.objects.all()
    return render(request,"main/all_plants.html",{"plants":plants})

#Plant Detail Page  
def plant_detail(request :HttpRequest , plant_id):
    plant = Plant.objects.get(pk=plant_id)
    
    return render(request,"main/plant_detail.html",{"plant":plant})


# Plant Search Page (by name), Bonus -> Add search by category, and is_edible in the Plant Search Page 

def search_page(request :HttpRequest):
    plants=[]
    
    if "search" in request.GET:
        plants = Plant.objects.filter(name__icontains=request.GET["search"])

    return render(request,"main/search.html",{"plants":plants})


# Add new plant page:
def new_plant(request :HttpRequest):
    
    if request.method == "POST":
        plant = Plant(
            # request.POST : access form data submitted via POST requests 
            name = request.POST["name"],
            about = request.POST["about"],
            used_for = request.POST["used_for"],
            image = request.FILES["image"],
            category = request.POST.get("category","Tree"),
            is_edible = request.POST["is_edible"],
        )
        plant.save()
        redirect("main:home_page")
        
    return render(request,"main/new_plant.html",{"categories":Plant.categories.choices})


# Update plant page : 
def update_plant(request :HttpRequest,plant_id):
        
    plant = Plant.objects.get(pk=plant_id)   
    
    if request.method =="POST":
    
        # request.POST : access form data submitted via POST requests 
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        plant.image = request.FILES.get("image",plant.image)
        plant.category = request.POST.get("category","Tree")
        plant.is_edible = request.POST.get("is_edible",False)
        plant.save()
        return redirect("main:home_page")
      
    return render(request,"main/update_plant.html",{"plant":plant ,"categories":Plant.categories.choices})


# Delete Plant :
def delete_plant(request :HttpRequest,plant_id):
    
    plant = Plant.objects.get(pk=plant_id)
    plant.delete()
    
    return redirect("home_page.html")

# # #  Bonus pages :

# Contact Us page :
def contact_page():
    return

# Contact Us Messages page :
def contact_messages():
    return



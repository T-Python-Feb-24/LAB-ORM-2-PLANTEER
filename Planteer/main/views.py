import os
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
from .models import Plant,Contact,Comment
from datetime import datetime

# Create your views here.
def index_page(request:HttpRequest):
    print(request.GET)

    plants=Plant.objects.all()[0:3]
    lastest_comments=Comment.objects.order_by("-created_at")[:5]    
    return render(request,'main/index.html',{"plants":plants,"lastest_comments":lastest_comments})

def add_plants(request:HttpRequest):
    if request.method=="POST":
        try:
            new_plant = Plant(name=request.POST["name"], about=request.POST["about"], categore=request.POST["categore"], used_for=request.POST["used_for"], image=request.FILES["image"], is_edible=request.POST.get("is_edible", False))         
            new_plant.save()
            return redirect("main:all_plants")           
        except Exception as e:
            print(e)
    return render(request, "main/add_plants.html", {"categories": Plant.categories.choices})

def add_plants_view(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_plant = Plant(name=request.POST["name"], about=request.POST["about"], categore=request.POST["categore"], used_for=request.POST["used_for"], image=request.FILES["image"], is_edible=request.POST.get("is_edible", False))         
            new_plant.save()

        except Exception as e:
            print(e)

    return render(request, "main/add_plants.html")

def all_plants(request:HttpRequest):
    plants=Plant.objects.all()

    count = plants.count()

    return render(request,"main/all_plants.html",{"plants":plants, 'count': count})



def plant_detail(request ,plant_id):
    
    try:
        #getting a  post detail
        plant = Plant.objects.get(pk=plant_id)
        comments=Comment.objects.filter(plant=plant)
        count = comments.count()

  
    except Exception as e:
        print(e)
    
    return render(request,"main/plant_details.html",{"plant" : plant,"comments":comments,"count":count})

def delete_plant_view(request:HttpRequest, plant_id):

    try:
        plant = Plant.objects.get(pk=plant_id)        
        plant.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:all_plants")


def update_plant_view(request:HttpRequest, plant_id):

    plant = Plant.objects.get(pk=plant_id)

    if request.method == "POST":
        try:
            plant.name=request.POST["name"]
            plant.about=request.POST["about"]
            plant.categore=request.POST["categore"]
            plant.used_for=request.POST["used_for"]
            plant.image=request.FILES.get("image",plant.image)
            plant.is_edible=request.POST.get("is_edible", False)
            plant.save()
            return redirect("main:plants_details", plant_id=plant.id)
        except Exception as e:
            print(e)

    
    return render(request, 'main/update_plant.html', {"plant" : plant, "categories" : Plant.categories.choices})






def search_page(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    plants = Plant.objects.all()

    if query:
        plants = plants.filter(name__icontains=query)

    if category:
        plants = plants.filter(categore=category)

    if is_edible:
        is_edible = bool(int(is_edible))  
        plants = plants.filter(is_edible=is_edible)

    count = plants.count()

    return render(request, 'main/search.html', {'plants': plants, 'count': count})

def contact_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Contact object and save it to the database
        contact = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
        contact.save()

        return redirect('main:index_page')

    return render(request, "main/contact.html")



def show_message_page(request):
    messages = Contact.objects.all().order_by('-created_at')
    return render(request, "main/show_message_page.html", {'messages': messages})



def add_comment_view(request: HttpRequest ,plant_id):
    if request.method == "POST":
        plant= Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant=plant,full_name=request.POST["full_name"], content=request.POST["content"])
        new_comment.save()
    
    
    return redirect("main:plants_details",plant_id=plant.id)
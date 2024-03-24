from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant,Contact,Comment
# Create your views here.

def home_page(requset:HttpRequest):
    
    plants=Plant.objects.all().order_by('-created_at')[0:3]
    
    return render(requset,"main/home_page.html",{"plants":plants})


def all_plants(requset:HttpRequest):
    if "cat" in requset.GET:
        plant = Plant.objects.filter(categroy = requset.GET["cat"])
    else:
        plant = Plant.objects.all().order_by("-created_at")
    
    return render(requset, "main/all_plants.html", {"plants" : plant, "Category":Plant.categories.choices})



def detail_plants(requset:HttpRequest,plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        comments=Comment.objects.filter(plant=plant)
        related = Plant.objects.filter(category=plant.categroy).exclude(id=plant_id)[:3]
    except Plant.DoesNotExist:
        pass
    except Exception as e:
        print(e)
    return render(requset ,"main/detail_plants.html", {"plant":plant,"comments":comments ,"related":related})


def plants_search(requset:HttpRequest):
    plants = []

    if "search" in requset.GET:
        plants = Plant.objects.filter(name__contains=requset.GET["search"])


    return render(requset, "main/plants_search.html", {"plants" : plants})
    



def add_plants(requset:HttpRequest):
    if requset.method== 'POST':
        try:
            new_plants =Plant(
                name=requset.POST["name"], 
                about=requset.POST["about"],
                used_for=requset.POST["used_for"], 
                is_edible=requset.POST.get("is_edible", False), 
                image=requset.FILES["image"],
                categroy=requset.POST["category"]
            )
            new_plants.save()
            return redirect("main:home_page")
        except Exception as e:
            print(e)

    return render(requset, "main/add_plants.html", {"Category":Plant.categories.choices})

    

def update_plants(requset:HttpRequest,plant_id):
    
    plant=Plant.objects.get(pk=plant_id)
    if requset.method== 'POST':
        try:
            plant.name=requset.POST["name"], 
            plant.about=requset.POST["about"],
            plant.used_for=requset.POST["used_for"], 
            plant.is_edible=requset.POST.get("is_edible", False), 
            plant.image=requset.FILES["image"],
            plant.categroy=requset.POST['categroy']
            plant.save()
            return redirect("main:detail_plant", plant_id=plant.id)
        except Exception as e:
            print(e)

    return render(requset, "main/update_plants.html", {"plant":plant, "Category":Plant.categories.choices})


def delete_plants(requset:HttpRequest,plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        plant.delete()
    except Exception as e:
        print(e)
    return redirect('main:home_page')
    

def contact(requset:HttpRequest):
    if requset.method== 'POST':
        try:
            contact =Contact(
                first_name=requset.POST["first_name"], 
                last_name=requset.POST["last_name"],
                message=requset.POST[" message"],  
                email=requset.POST["email"],
            )
            contact.save()
            return redirect("main:contact_messages")
        except Exception as e:
            print(e)

    return render(requset, "main/contact.html",{"contact":contact} )

def contact_messages(requset:HttpRequest):
    try:
        contact= Contact.objects.all()
    except Exception as e:
            print(e)
    return render( requset,'main/contact_messages.html',{"contact":contact})


def add_comment(request:HttpRequest, plant_id):

    if request.method == "POST":
        try:
            plant_object = Plant.objects.get(pk=plant_id)
            new_comment = Comment(plant=plant_object,full_name=request.POST["full_name"], content=request.POST["content"])
            new_comment.save()
        except Exception as e:
                print(e)
    
    return redirect("main:detail_plants", plant_id=plant_object.id)
    
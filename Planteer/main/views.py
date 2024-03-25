from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
# Create your views here.
from .models import Plant, Contact, Comment

def home_view(request: HttpRequest):

    plants = Plant.objects.all().order_by('-published_at')[0:3]
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, "main/index.html", {"plants" : plants, "comments" : comments})

def add_plant_view(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_plant = Plant(title=request.POST["title"], 
                            content=request.POST["content"], 
                            is_edible=request.POST.get("is_edible", False), 
                            category= request.POST["category"],  
                            poster=request.FILES["poster"])
            new_plant.save()
            return redirect("main:index_view")
        except Exception as e:
            print(e)

    return render(request, "main/add_plant.html", {"categories" : Plant.categories.choices})

def plant_detail_view(request:HttpRequest, plant_id):

    try:
        plant = Plant.objects.get(pk=plant_id)
        comments = Comment.objects.filter(plant=plant)
    except Plant.DoesNotExist:
            return render(request,"main/not_found.html")
    except Exception as e:
        print(e)


    return render(request, "main/detail.html", {"plant" : plant, "comments" : comments})

def update_plant_view(request:HttpRequest, plant_id):

    plant = Plant.objects.get(pk=plant_id)

    if request.method == "POST":
        try:
            
            plant.title = request.POST["title"]
            plant.content = request.POST["content"]
            plant.is_edible = request.POST.get("is_edible", False)
            plant.category = request.POST["category"]
            plant.poster = request.FILES.get("poster", plant.poster)
            plant.save()
            return redirect("main:plant_detail_view", plant_id=plant.id)
        except Exception as e:
            print(e)

    
    return render(request, 'main/update.html', {"plant" : plant, "categories" : Plant.categories.choices})

def delete_plant_view(request:HttpRequest, plant_id):

    try:
        plant = Plant.objects.get(pk=plant_id)
        plant.delete()
    except Plant.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)
    

    return redirect("main:home_view")


def all_plant_view(request: HttpRequest):

    
    if "cat" in request.GET:
        plants = Plant.objects.filter(category=request.GET["cat"])
    else:
        plants = Plant.objects.all()


    return render(request, "main/all_plants.html", {"plants" : plants, "categories" : Plant.categories.choices})


def plants_search_view(request:HttpRequest):
    plants = []

    if "search" in request.GET:
        plants = Plant.objects.filter(title__contains=request.GET["search"])

    if "date" in request.GET and len(request.GET["date"]) > 4:
        first_date = date.fromisoformat(request.GET["date"])
        end_date = first_date + timedelta(days=1)
        plants = plants.filter(published_at__gte=first_date, published_at__lt=end_date)


    return render(request, "main/search.html", {"plants" : plants})

def contact_view(request:HttpRequest):
    if request.method == "POST":
            new_message = Contact(first_name=request.POST["first_name"],
                                  last_name=request.POST["last_name"], 
                                  email=request.POST["email"],  
                                  message= request.POST["message"],)
            
            new_message.save()

    return render(request, "main/contact.html")

def message_view(request:HttpRequest):

    messages = Contact.objects.all()
    
    return render(request, "main/message.html", {"messages" : messages})

def add_comment_view(request:HttpRequest, plant_id):
    if request.method == "POST":
        plant_object = Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant=plant_object,full_name=request.POST["full_name"],
                              content=request.POST["content"])
        
        new_comment.save()

        return redirect("main:plant_detail_view", plant_id=plant_object.id)
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Plant, Comment
# Create your views here.

# page 1: Home page
def index_view(request: HttpRequest):

    #limiting the result using slicing
    plants = Plant.objects.all().order_by('-created_at')[0:3]
    return render(request, "plants/index.html", {"plants" : plants})


# page 2: Add new plant page
def add_plant_view(request:HttpRequest):
    if request.method == 'POST':
        try:    
            plant = Plant(
                name = request.POST["name"],
                about = request.POST["about"],
                used_for = request.POST["used_for"],
                image = request.FILES["image"],
                category = request.POST["category"],
                native_to = request.POST["native_to"],
                is_edible = request.POST.get("is_edible", False),
            )
            plant.save()
            return redirect("plants:index_view")
        except Exception as e:
            print(e)
    return render(request, "plants/add_plant.html", {"categories" : Plant.categories.choices})


# page 3: Update plant page
def update_plant_view(request:HttpRequest, plant_id):
    
    plant = Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        try:
            plant.name = request.POST["name"]
            plant.about = request.POST["about"]
            plant.used_for = request.POST["used_for"]
            plant.image = request.FILES.get("image", plant.image)
            plant.category = request.POST["category"]
            plant.native_to = request.POST["native_to"]
            plant.is_edible = request.POST.get("is_edible", False)
            plant.save()
            return redirect("plants:plant_detail_view", plant_id = plant.id)
        except Exception as e:
            print(e)
    return render(request, "plants/update_plant.html", {"plant" : plant, "categories" : Plant.categories.choices})


# page 4: Plant Detail Page
def plant_detail_view(request:HttpRequest, plant_id):
    try:
        plant =Plant.objects.get(pk=plant_id)
        related_plants = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)[0:3]   
        comments = Comment.objects.filter(plant=plant)
    except Plant.DoesNotExist:
        plant = None
    except Exception as e:
        print(e)
    return render(request, "plants/plant_detail.html", {"plant" : plant, "related_plants" : related_plants, "comments" : comments})


# page 5: Plant Search Page
def plant_search_view(request:HttpRequest):
    plants=[]
    if "search" in request.GET:
        plants = Plant.objects.filter(name__contains=request.GET["search"])
    
    if 'cat' in request.GET:
        posts = Plant.objects.filter(category = request.GET['cat'])

    return render(request, "plants/plant_search.html",{"plants" : plants, 'categories': Plant.categories.choices} )

# page 6: All Plants page
def all_plants_view(request:HttpRequest):
    plants = Plant.objects.all()
    return render(request, "plants/all_plants.html", {"plants" : plants})

# function 7: Delete Plant

def delete_plant_view(request:HttpRequest, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        plant.delete()
    except Exception as e:
        print(e)
    return redirect("plants:index_view")


def add_comment_view(request:HttpRequest, plant_id):

    if request.method == "POST":

        plant_key = Plant.objects.get(pk=plant_id)
        comment = Comment(
            plant=plant_key, 
            full_name=request.POST["full_name"], 
            content=request.POST["content"],
        )
        comment.save()
    return redirect("plants:plant_detail_view", plant_id=plant_key.id)

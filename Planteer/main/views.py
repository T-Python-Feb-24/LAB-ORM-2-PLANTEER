from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant, Contact, Comment

def index_view(request: HttpRequest):
    print(request.GET)
    plants = Plant.objects.all()


    return render(request, "main/index.html", {"plants" : plants})

def contact_view(request:HttpRequest):

    if request.method == 'POST':
        try:
            new_message = Contact(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                message = request.POST['message']
            )
            new_message.save()
            return redirect("main:all_messages_view")
        except Exception as e:
            print(e)
    return render(request, "main/contact.html")
def all_plants_view(request: HttpRequest):
    plants = Plant.objects.all()
    return render(request,"main/all_plants.html", { 'plants' : plants })
   


def add_plant_view(request:HttpRequest):

    if request.method == 'POST':
        try:
            new_plant= Plant(
                name = request.POST["name"],
                about = request.POST["about"],
                used_for = request.POST["used_for"],
                image = request.FILES["image"],
                category = request.POST["category"],
                is_edible = request.POST.get("is_edible", True)
            )
            new_plant.save()
            return redirect("main:index_view")
        except Exception as e:
            print(e)
    return render(request, "main/add_plant.html", {"categories" : Plant.categories.choices})

def plant_detail_view(request: HttpRequest, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        comments = Comment.objects.filter(plant=plant)
        plants_with_same_cat = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)
    except Plant.DoesNotExist:
        return render(request, "main/not_exist.html")
    except Exception as e:
        print(e)
    return render(request, "main/plant_detail.html", {"plant": plant, "Comment": comments, "plants_with_same_cat": plants_with_same_cat})

def update_plant_view(request:HttpRequest, plant_id):

    plant = Plant.objects.get(pk=plant_id)

    if request.method == 'POST':
        try:
            plant.name = request.POST['name']
            plant.about = request.POST['about']
            plant.used_for = request.POST['used_for']
            plant.category = request.POST['category']
            plant.is_edible = request.POST.get("is_edible", True)
            plant.save()
            return redirect("main:plant_detail_view", plant_id=plant.id)
        except Exception as e:
            print(e)

    return render(request, "main/update_plant.html", {"plant" : plant, "categories": Plant.categories.choices})


def delete_view(request: HttpRequest, plant_id: int):
    try:
        plant = Plant.objects.get(pk=plant_id)
        plant.delete()
    except Plant.DoesNotExist:
        pass
    except Exception as e:
        print(e)

    return redirect("main:index_view")


def plants_search_view(request:HttpRequest):
    search_query = request.GET.get("search_query")

    search_category = request.GET.get("category")

    search_is_edible = request.GET.get('is_edible')

    plants = Plant.objects.all()

    if search_query:
        plants = plants.filter(name__icontains=search_query)

    if search_category:
        plants = plants.filter(category=search_category)

    if search_is_edible is not None:
        search_is_edible = search_is_edible.lower() == 'true'
        plants = plants.filter(is_edible=search_is_edible)

    return render(request, "main/plants_search.html", {"plants":plants, "search_query": search_query, "categories" : Plant.categories.choices})

def messages_view (request):
    messages = Contact.objects.all().order_by('created_at')
    return render(request, "main/messages.html", {'messages': messages})

def add_comment_view(request: HttpRequest ,plant_id):
    if request.method == "POST":
        plant= Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant=plant,full_name=request.POST["full_name"], content=request.POST["content"])
        new_comment.save()


    return redirect("main:plants_details",plant_id=plant.id)
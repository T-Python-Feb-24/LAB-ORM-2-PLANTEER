from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant, Comment
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


# HOME PAGE 
def home_page(request: HttpRequest):

    print(request.GET)
    plants= Plant.objects.all()
    plants = Plant.objects.all().order_by('-created_at')[0:3]
    comment=Comment.objects.order_by("-created_at")[0:3]
    # comments = Comment.objects.all().order_by('-created-at')[0:3]
    # comments = Comment.objects.all()[0:3]

    return render(request, "main/home_page.html", {"plants" : plants , "comments" : comment})





# DISPLAY ALL PLANTS 
def all_plants(request: HttpRequest):

    if "cat" in request.GET:
        plants = Plant.objects.filter(category=request.GET["cat"])
    else:
        plants = Plant.objects.all().order_by("-created_at")

    return render(request, "main/all_plants.html", {"plants" : plants, "categories" : Plant.categories.choices})



# ADD PLANT 
def add_plant(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_plant = Plant(
                name = request.POST["name"], 
                about = request.POST["about"],
                used_for = request.POST["used_for"],
                image = request.FILES.get("image", Plant.image.field.default),
                is_edible = request.POST.get("is_edible", False), 
                category = request.POST['category']
            )

            new_plant.save()
            return redirect("main:home_page")
        except Exception as e:
            print(e)

    return render(request, "main/add_plant.html", {"categories" : Plant.categories.choices})



# PLANTS DETAELS 
def plant_detail(request:HttpRequest, plant_id):

    try:
        plant = Plant.objects.get(pk=plant_id)
        comment=Comment.objects.filter(plant=plant)
    except Plant.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)

    return render(request, "main/plant_detail.html", {"plant" : plant , "comments" : comment})




# UPDATE PLANT
def update_plant(request:HttpRequest, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        
        try:
            plant.name = request.POST["name"]
            plant.about = request.POST["about"]
            plant.used_for = request.POST["used_for"]
            plant.image = request.FILES.get("image", plant.image)
            plant.category = request.POST["category"]
            plant.is_edible = request.POST.get("is_edible", False )
            plant.save()
            return redirect("main:plant_detail", plant_id=plant.id)
        except Exception as e:
            print(e)

    return render(request, 'main/update_plant.html', {"plant" : plant, "categories" : Plant.categories.choices})



# DELETE PLANT 
def delete_plant(request:HttpRequest, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        plant.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:home_page")



# ALL PLANTS SEARCH 
def all_search(request: HttpRequest):
    if request.method == 'GET':
        category = request.GET.get('category', '')

        if category:
            plants = Plant.objects.filter(category=category)
        else:
            plants = Plant.objects.all()
        return render(request, 'main/all_search.html', {'plants': plants, 'category': category})

    return HttpResponse('Invalid request')



# PLANTS SEARCH 
def plant_search(request: HttpRequest):
    if request.method == 'GET':
        category = request.GET.get('category', '')

        if category:
            plants = Plant.objects.filter(category=category)
        else:
            plants = Plant.objects.all()
        return render(request, 'main/plant_search.html', {'plants': plants, 'category': category})

    return HttpResponse('Invalid request')


# COMMENTS 
def add_comment(request:HttpRequest, plant_id):

    if request.method == "POST":
        #add new comment
        plant_object = Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant=plant_object,full_name=request.POST["full_name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("main:plant_detail", plant_id=plant_id)



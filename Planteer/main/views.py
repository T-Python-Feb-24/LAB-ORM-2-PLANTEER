from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant, Contact, Comment
# Create your views here.

def index_view(request : HttpRequest):
    #getting the Query Parameters
    print(request.GET)

    plants = Plant.objects.order_by('created_at')[:3]

    return render(request, "main/index.html", {"plants" : plants})

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

def plant_detail_view(request:HttpRequest, plant_id):

    try:
        #getting a plant to display its detail
        plant = Plant.objects.get(pk=plant_id)

        #here getting the plants for 'related plants'
        plants_with_same_cat = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)

        #here we getting the Comments
        comments = Comment.objects.filter(plant = plant) #the first plant here its a column from the table of Comment and the second its the object from Plant
    except Plant.DoesNotExist:
        return render(request, "main/not_exist.html")
    except Exception as e:
        print(e)
    return render(request, "main/plant_detail.html", {"plant": plant, "plants_with_same_cat":plants_with_same_cat, "comments":comments})

def update_plant_view(request:HttpRequest, plant_id):

    try:
        # Attempt to get the plant
        plant = Plant.objects.get(pk=plant_id)
    except Plant.DoesNotExist:
        return render(request, "main/not_exist.html")

    if request.method == 'POST':
        try:
            # Update the plant's attributes
            plant.name = request.POST['name']
            plant.about = request.POST['about']
            plant.used_for = request.POST['used_for']
            plant.category = request.POST['category']
            plant.is_edible = request.POST.get("is_edible", True)
            plant.save()
            return redirect("main:plant_detail_view", plant_id=plant.id)
        except Exception as e:
            # Handle other exceptions
            print(e)

    return render(request, "main/update_plant.html", {"plant" : plant, "categories": Plant.categories.choices})

def delete_plant_view(request:HttpRequest, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        plant.delete()
    except Plant.DoesNotExist:
        return render(request, "main/not_exist.html")
    except Exception as e:
        print(e)

    return redirect("main:index_view")

def all_plant_view(request:HttpRequest):

    #the categories that user will choose between them to filter
    selected_category = request.GET.get("cat")

    #get the plants to display it
    plants = Plant.objects.filter(category=selected_category) if selected_category else Plant.objects.all()

    return render(request, "main/all_plant.html", {"plants" : plants, "selected_category" : selected_category, "categories" : Plant.categories.choices})

def search_view(request:HttpRequest):
    # to search by name
    search_query = request.GET.get("search_query")

    #to search by category
    search_category = request.GET.get("category")

    #to search by is_edible
    search_is_edible = request.GET.get('is_edible')

    plants = Plant.objects.all()

    if search_query:
        plants = plants.filter(name__icontains=search_query)
    
    if search_category:
        plants = plants.filter(category=search_category)
    
    if search_is_edible is not None:
        search_is_edible = search_is_edible.lower() == 'true'
        # Filter plants based on is_edible
        plants = plants.filter(is_edible=search_is_edible)
    
    return render(request, "main/search_plant.html", {"plants":plants, "search_query": search_query, "categories" : Plant.categories.choices})

def contact_us_view(request:HttpRequest):
    
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

def all_messages_view(request:HttpRequest):

    messages = Contact.objects.all()

    return render(request, "main/all_messages.html", {"messages":messages})

def add_comment_view(request:HttpRequest, plant_id):
    if request.method == 'POST':
        #add a new comment
        plant = Plant.objects.get(pk=plant_id)
        new_comment = Comment(
            plant = plant,#the first plant from Comment table of a column called 'plant', and the other plant its the object from Plant
            full_name = request.POST["full_name"],
            content = request.POST["content"]
        )
        new_comment.save()
    
    return redirect("main:plant_detail_view", plant_id=plant.id)
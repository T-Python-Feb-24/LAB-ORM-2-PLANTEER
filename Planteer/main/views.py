
from django.http import HttpResponseNotFound,HttpRequest
from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator
from .models import  Plant 
from .models import Contact, Comment
from favorites.models import Favorite

def home(request):
    print(request.GET)
    plants = Plant.objects.all()
    
    latest_comments = Comment.objects.order_by('-created_at')[:5]
    
    paginator = Paginator(plants, 3) 

    page_number = request.GET.get('page')
    plants = paginator.get_page(page_number)




    return render(request, 'main/index.html', {'plants': plants, 'latest_comments': latest_comments})



def add_plant(request):
    if not request.user.is_staff:
        # Render home template for non-staff users
        return render(request, "main/home.html")

    if request.method == 'POST':
        try:
            new_plant = Plant(name=request.POST["name"], about=request.POST["about"],used_for = request.POST["used_for"], created_at=request.POST.get("created_at", False), category= request.POST["category"],  image=request.FILES["image"],is_edible = request.POST.get('is_edible') == 'True')
            new_plant.save()
            return redirect("main:home")
        except Exception as e:
            print(e)

    return render(request, "main/add_plant.html", {"categories" : Plant.categories.choices})

    

def plant_detail(request, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        related_plants = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)[:3]
        is_favored = request.user.is_authenticated and  Favorite.objects.filter(user=request.user, plant=plant).exists()
        plant = Plant.objects.get(pk=plant_id)
        comments = Comment.objects.filter(plant=plant)
        
        return render(request, 'main/plant_detail.html', {'plant': plant, 'related_plants': related_plants,  "comments" : comments})
    except Plant.DoesNotExist:
        return HttpResponseNotFound('Plant not found')
    
def update_plant(request, plant_id):
    if not request.user.is_staff:
        return render(request, "main/home.html")

    plant = get_object_or_404(Plant, pk=plant_id)

    if request.method == "POST":
        try:
            
            plant.name = request.POST["name"]
            plant.about = request.POST["about"]
            plant.used_for = request.POST["used_for"]
            plant.is_edible = request.POST.get('is_edible') == 'True'
            plant.category = request.POST["category"]
            plant.image = request.FILES.get("image", plant.image)
            plant.save()
            return redirect("main:plant_detail", plant_id=plant.id)
        except Exception as e:
            print(e)

    return render(request, 'main/update_plant.html', {'plant': plant})



def delete_plant(request, plant_id):
    # Check if the user is staff
    if not request.user.is_staff:
        # Render home template for non-staff users
        return render(request, "main/home.html")

    # Retrieve the plant object
    plant = get_object_or_404(Plant, pk=plant_id)
    
    # Delete the plant
    plant.delete()

    # Redirect to the home page after successful deletion
    return redirect('main:home')


def all_plants_view(request):
    if "cat" in request.GET:
        plants = Plant.objects.filter(category=request.GET["cat"])
    else:
        plants = Plant.objects.all()

    return render(request, "main/all_plants.html", {"plants" : plants, "categories" : Plant.categories.choices})

    

def search_plants(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    
    plants = Plant.objects.all()
    if query:
        plants = plants.filter(name__icontains=query)
    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=is_edible)

    return render(request, 'main/search_plants.html', {'search_results': plants, 'query': query})

def contact_view(request):
    if request.method == "POST":
       
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

       
        contact = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
        contact.save()

       
        return redirect('main:contact_success')  

    
    return render(request, 'main/contact.html')

def contact_success(request):
     return render(request, 'main/contact_success.html')
 
def add_comment(request: HttpRequest , plant_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login_user")

    if request.method == "POST":
        plant_object = Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant=plant_object,user=request.user,content=request.POST["content"])
        new_comment.save()
        
    return redirect("main:plant_detail", plant_id=plant_object.id)

def message_view(request:HttpRequest):
    if not request.user.is_staff:
        return render(request, "main/home.html")

    messages = Contact.objects.all()

    return render(request, "main/message.html", {"messages" : messages})
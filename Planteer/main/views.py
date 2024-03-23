
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator
from .models import  Plant 
from .models import Contact

def home(request):
    print(request.GET)
    plants = Plant.objects.all()
    
    
    
    paginator = Paginator(plants, 3) 

    page_number = request.GET.get('page')
    plants = paginator.get_page(page_number)




    return render(request, 'main/index.html', {'plants': plants})



def add_plant(request):
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

        
        return render(request, 'main/plant_detail.html', {'plant': plant, 'related_plants': related_plants})
    except Plant.DoesNotExist:
        return HttpResponseNotFound('Plant not found')
def update_plant(request, plant_id):
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
    plant = get_object_or_404(Plant, pk=plant_id)
    plant.delete()
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
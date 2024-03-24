from django.shortcuts import render, redirect, get_object_or_404
from .models import Plant ,Comment
from django.http import HttpRequest, HttpResponse
from django.utils import timezone  
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

def home(request):
    plants = Plant.objects.filter(is_edible=True).order_by('-create_at')

    paginator = Paginator(plants, 3)
    page_number = request.GET.get('page')
    
    latest_comments = Comment.objects.all().order_by('-created_at')[:4]
    
    try:
        paginated_plants = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_plants = paginator.page(1)
    except EmptyPage:
        paginated_plants = paginator.page(paginator.num_pages)

    context = {
        'plants': paginated_plants,
        'latest_comments': latest_comments, # Include latest comments
    }
    return render(request, 'main/home.html', context)


def add_plant(request):

    CATEGORY_CHOICES = Plant.CATEGORY_CHOICES  

    if request.method == 'POST':
        name = request.POST.get('name')
        about = request.POST.get('about')
        user_for = request.POST.get('user_for')
        category = request.POST.get('category')
        is_edible_str = request.POST.get('is_edible')
        image = request.FILES.get('image')  
        is_edible = is_edible_str.lower() == 'true'
        
        plant = Plant.objects.create(
            name=name,
            about=about,
            user_for=user_for,
            category=category,
            is_edible=is_edible,
            image=image,  
            create_at=timezone.now()
        )
        
        return redirect('home')
    
    return render(request, 'main/add_plant.html', {'CATEGORY_CHOICES': CATEGORY_CHOICES})

#################################################################

def plant_detail(request, pk):
    try:
        plant = get_object_or_404(Plant, pk=pk)
        comments = Comment.objects.filter(plant=plant)
    except Plant.DoesNotExist:
        raise Http404("Plant does not exist")
    
    return render(request, 'main/plant_detail.html', {'plant': plant, "comments": comments})

def plant_update(request: HttpRequest, pk):
    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'POST':
        try:
            plant.name = request.POST.get('name')
            plant.about = request.POST.get('about')
            plant.user_for = request.POST.get('user_for')
            plant.category = request.POST.get('category')
            plant.is_edible = request.POST.get('is_edible') == 'on'  
            new_image = request.FILES.get('image')  
            
            if new_image:
                plant.image = new_image
            
            plant.save()
            return redirect('plant_detail', pk=plant.pk)
        except Exception as e:
            print(e)

    return render(request, 'main/update_plant.html', {'plant': plant})

def plant_delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        plant.delete()
        return redirect('home')
    return render(request, 'main/plant_delete_confirm.html', {'plant': plant})

def all_plants(request):
    search_query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    edible_filter = request.GET.get('edible', '')  

    if search_query:
        plants = Plant.objects.filter(name__icontains=search_query)
    else:
        plants = Plant.objects.all()

    if category_filter:
        plants = plants.filter(category=category_filter)
    
    if edible_filter in ['true', 'false']:
        edible_bool = edible_filter == 'true'
        plants = plants.filter(is_edible=edible_bool)
    
    paginator = Paginator(plants, 3)  
    page = request.GET.get('page')

    try:
        plants = paginator.page(page)
    except PageNotAnInteger:
        plants = paginator.page(1)
    except EmptyPage:
        plants = paginator.page(paginator.num_pages)

    category_counts = Plant.objects.values('category').annotate(count=Count('category'))

    context = {
        'plants': plants,
        'category_counts': category_counts,
        'search_query': search_query,
        'selected_category': category_filter,  
    }
    return render(request, 'main/all_plants.html', context)

def contact_us(request):

    return render( request, 'main/contact_us.html')

def add_comment(request, plant_id):
    if request.method == "POST":
        try:
            plant_object = get_object_or_404(Plant, pk=plant_id)
            full_name = request.POST.get('full_name')
            content = request.POST.get('content')
            new_comment = Comment.objects.create(plant=plant_object, full_name=full_name, content=content)
            return redirect('plant_detail', pk=plant_id)
        except KeyError:
            pass
    
    return redirect('plant_detail', pk=plant_id)


from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant,Comment
#from datetime import date, timedelta
# Create your views here.

# Create your views here.

# Create your views here.

def home(request:HttpRequest):
    
    plants = Plant.objects.all()[0:3]

    return render(request,'main/index.html', {'plants' : plants})

def add_plant(request:HttpRequest):
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
            
        except Exception as e:
            print(e)
        return redirect("main:home")

    return render(request, "main/add_plant.html", {'category' : Plant.Categories.choices})

def all_plant(request:HttpRequest):
    if "cat" in request.GET:
        plants = Plant.objects.filter(category = request.GET["cat"])
    else:
        plants = Plant.objects.all().order_by("-created_at") 
    
        #calculate the page content
    limit = 3
    pages_count = [str(n) for n in range(1, round(plants.count()/limit)+1)]
    start = (int(request.GET.get("page", 1))-1)*limit
    end = (start)+limit

    print(list(pages_count))


    #apply the limit/slicing
    plants = plants[start:end]

    # print(start, end)

    return render(request, "main/all_plants.html", {"plants" : plants, "category" : Plant.Categories.choices, "pages_count":pages_count})

def  plant_detail(request:HttpRequest, plant_id):
        try:
            #getting a  post detail
            plant = Plant.objects.get(pk=plant_id)
            related = Plant.objects.all()
            comments = Comment.objects.filter(plant= plant) #this is to get the comments on the above post using filter
        except Plant.DoesNotExist:
            return render(request, "404.html")
        except Exception as e:
            print(e)
        

        return render(request, "main/post_detail.html", {"plant" : plant, "related": related, "comments": comments})

def update_plant(request:HttpRequest, plant_id):
        try:
            plant = Plant.objects.get(pk=plant_id)
        except Plant.DoesNotExist:
            return render(request, "404.html")

        if request.method == "POST":
            try:
                plant.name = request.POST["name"]
                plant.about = request.POST["about"]
                plant.used_for = request.POST["used_for"]
                plant.image = request.FILES.get('image', plant.image)
                plant.is_edible = request.POST.get("is_edible", False)
                plant.category = request.POST['category']
                plant.save()
            except Plant.DoesNotExist:
                return render(request, "404.html")
            except Exception as e:
                print(e)
            return redirect("main:plant_detail", plant_id= plant.id)

        return render(request, 'main/update_post.html', {"plant" : plant, 'categories' : Plant.Categories.choices})

def delete_plant(request:HttpRequest, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
    except Plant.DoesNotExist:
        return render(request, "404.html")
    
    try:
        plant.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:home")

def search(request: HttpRequest):
    plants = []
    try: 
        if "search" in request.GET:
            plants = Plant.objects.filter(name__contains=request.GET["search"])

        
        # if "date" in request.GET and len(request.GET["date"]) > 4:
        #     first_date = date.fromisoformat(request.GET["date"])
        #     end_date = first_date + timedelta(days=1)
        #     plants = plants.filter(created_at__gte=first_date, created_at__lt=end_date)
    except Exception as e:
        print(e)
    
    context = {"plants" : plants}
    return render(request,"main/Search_Result.html", context)


def add_comment(request:HttpRequest, plant_id):

    if request.method == "POST":
        #add new comment
        post_object = Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant=post_object,full_name=request.POST["full_name"], content=request.POST["content"])
        new_comment.save()

    return redirect("main:plant_detail", plant_id=post_object.id)
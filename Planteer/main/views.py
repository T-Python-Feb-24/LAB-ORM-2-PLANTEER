

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant,Comment
# Create your views here.
from .models import Plant, Comment, Contact
# from favorites.models import Favorite



def home(request:HttpRequest):
    #get user info
    if request.user.is_authenticated:
        print(request.user.first_name)
    comments=Comment.objects.all()[0:3]
    plants = Plant.objects.all()[0:3]

   

    return render(request,'main/index.html', {'plants' : plants ,'comments' : comments})

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
        comments = Comment.objects.filter(plant=plant) #this is to get the comments on the above post using filter
        related_posts = Plant.objects.filter(category=plant.category).exclude(id=plant.id) #get related posts
        # is_favored = request.user.is_authenticated and  Favorite.objects.filter(user=request.user, post=plant).exists()
    except Plant.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)


    return render(request, "main/post_detail.html", {"plant" : plant, "comments" : comments , "related" : related_posts  })

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

    object = Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        #add new comment
        print(object)
        new_comment = Comment(plant=object,user=request.user, content=request.POST["content"])
        new_comment.save()
    
    return redirect("main:plant_detail", plant_id=object.id)


# هذا contact

def user_message(request: HttpRequest):
    if not request.user.is_superuser:
        return render(request, "main/no_permission.html")
    
    con=Contact.objects.all()

    return render(request,"main/message.html", {"con" : con})

def contact_us(request: HttpRequest):
 if request.method=="POST":
        try:
            info=Contact(
            f_name=request.POST["f_name"],
            l_name=request.POST["l_name"],
            email=request.POST["email"],
            message=request.POST["message"],
            )
            info.save()
            return redirect('main:home')
        except Exception as e :
            print(e)
 return render(request,"main/contact.html")
    

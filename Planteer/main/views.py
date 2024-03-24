from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Plant, Contact, Comment
# Create your views here.

def home(request:HttpRequest):
    
    plants = Plant.objects.all().order_by('-created_at')[0:3]

    comments = Comment.objects.all().order_by('-created_at')[0:5]

    return render(request,'main/home.html', {'plants' : plants, "comments": comments})

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
    
    limit = 3
    pages_count = [str(n) for n in range(1, round(plants.count()/limit)+1)]
    start = (int(request.GET.get("page", 1))-1)*limit
    end = (start)+limit

    print(list(pages_count))

    plants = plants[start:end]

    return render(request, "main/all_plants.html", {"plants" : plants, "category" : Plant.Categories.choices, "pages_count":pages_count})

def plant_detail(request:HttpRequest, plant_id):
        try:
            #getting a  post detail
            plant = Plant.objects.get(pk=plant_id)
            related = Plant.objects.filter(category =  plant.category).exclude(pk=plant_id)[:4]

            comments = Comment.objects.filter(post=plant) #this is to get the comments on the above post using filter

        except Plant.DoesNotExist:
            return render(request, "404.html")
        except Exception as e:
            print(e)
        

        return render(request, "main/plant_detail.html", {"plant" : plant, "related": related, "comments": comments})

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

        return render(request, 'main/update_plant.html', {"plant" : plant, 'category' : Plant.Categories.choices})

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
    return render(request,"main/search.html", context)

def contact(request:HttpRequest):
        if request.method == 'POST':
            try:
                new_con = Contact(
                    first_name = request.POST["first"],
                    last_name = request.POST["last"],
                    email = request.POST["email"],
                    message = request.POST['message']
                )
                new_con.save()
                
            except Exception as e:
                print(e)
            
            # return redirect('main:message')
        return render(request, 'main/contact.html')

def messages(request:HttpRequest):
    message = Contact.objects.all()[0:3]

    return render(request,'main/messages.html', {'message' : message})

def add_comment(request:HttpRequest, plant_id):
    # try:
    #     comment_id = Comment.objects.get(pk=plant_id)
    # except Comment.DoesNotExist:
    #     comment_id = None

    if request.method == "POST":
        #add new comment

            comment = Plant.objects.get(pk=plant_id)
            new_comment = Comment(
            post=comment,
            full_name=request.POST["full_name"],
            content=request.POST["content"]
            )
            new_comment.save()

    return redirect("main:plant_detail", plant_id=comment.id)

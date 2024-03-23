# from django.shortcuts import render, redirect
# from django.http import HttpRequest, HttpResponse
# from datetime import date, timedelta
# # Create your views here.
# from .models import Post


# def index_view(request: HttpRequest):

#     #getting the Query Parameters
#     print(request.GET)

#     #limiting the result using slicing
#     posts = Post.objects.all().order_by('-published_at')[0:3]


#     return render(request, "main/index.html", {"posts" : posts})


# def all_posts_view(request: HttpRequest):

    
#     if "cat" in request.GET:
#         posts = Post.objects.filter(category=request.GET["cat"])
#     else:
#         posts = Post.objects.all()
    
#     #calculate the page content
#     limit = 3
#     pages_count = [str(n) for n in range(1, round(posts.count()/limit)+1)] #use list comprehension to convert number to string number
#     start = (int(request.GET.get("page", 1))-1)*limit
#     end = (start)+limit

#     print(list(pages_count))


#     #apply the limit/slicing
#     posts = posts[start:end]

#     # print(start, end)

#     return render(request, "main/all_posts.html", {"posts" : posts, "categories" : Post.categories.choices, "pages_count":pages_count})

# def add_post_view(request: HttpRequest):

#     if request.method == 'POST':
#         try:
#             new_post = Post(
#                 title=request.POST["title"], 
#                 content=request.POST["content"], 
#                 is_published=request.POST.get("is_published", False), 
#                 category= request.POST["category"],  
#                 poster=request.FILES.get("poster", Post.poster.field.default)
#                 )
#             new_post.save()
#             return redirect("main:index_view")
#         except Exception as e:
#             print(e)

#     return render(request, "main/add_post.html", {"categories" : Post.categories.choices})




# def post_detail_view(request:HttpRequest, post_id):

#     try:
#         #getting a  post detail
#         post = Post.objects.get(pk=post_id)
#     except Post.DoesNotExist:
#         return render(request, "main/not_found.html")
#     except Exception as e:
#         print(e)


#     return render(request, "main/post_detail.html", {"post" : post})


# def update_post_view(request:HttpRequest, post_id):

#     post = Post.objects.get(pk=post_id)

#     if request.method == "POST":
#         try:
            
#             post.title = request.POST["title"]
#             post.content = request.POST["content"]
#             post.is_published = request.POST.get("is_published", False)
#             post.category = request.POST["category"]
#             post.poster = request.FILES.get("poster", post.poster)
#             post.save()
#             return redirect("main:post_detail_view", post_id=post.id)
#         except Exception as e:
#             print(e)

    
#     return render(request, 'main/update_post.html', {"post" : post, "categories" : Post.categories.choices})


# def delete_post_view(request:HttpRequest, post_id):

#     try:
#         post = Post.objects.get(pk=post_id)
#         post.delete()
#     except Exception as e:
#         print(e)
    

#     return redirect("main:index_view")



# def search(request: HttpRequest):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         posts = Post.objects.filter(title__icontains=q)
#     else:
#         posts = Post.objects.all().order_by('-published_at')
    
#     return render(request,"main/Search_Result.html",{"posts":posts})

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
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
        except Plant.DoesNotExist:
            return render(request, "404.html")
        except Exception as e:
            print(e)
        

        return render(request, "main/post_detail.html", {"plant" : plant, "related": related})

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

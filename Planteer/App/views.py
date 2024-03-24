from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from datetime import date,timedelta
import math
# Create your views here.
from .models import Post
def home_page(request: HttpRequest):


    return render(request,"App/index.html")


def add_post_view(request:HttpRequest):
    if request.method=='POST':
        try:
            new_post=Post(Name=request.POST['Name'],
                        about=request.POST['about'],
                        used_for=request.POST['used_for'],
                        image = request.FILES['image'] ,
                        edible = request.post.get("edible"),
                        created_at = request.POST.get("created_at", False), )
            new_post.save()
            return redirect('App:home_page')
        except Exception as e:
            print(e)

    return render(request,'App/add_post.html',)#{"categories" : Post.categories.choices})








def post_detail_view(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "App/not_found.html")
    except Exception as e:
        print(e)


    return render(request, "App/post_detail.html", {"post" : post})






def update_post_view(request:HttpRequest, post_id):


    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        try:

            post.Name= request.POST["Name"]
            post.about= request.POST["about"]
            post.used_for= request.POST["used_for"]

            post.category = request.POST["category"]
            post.poster = request.FILES.get("poster", post.poster)
            post.save()
            return redirect("App:post_detail_view", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'App/update_post.html', {"post" : post, "categories" : Post.categories.choices})


def delete_post_view(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("App:index_view")




def posts_search_view(request:HttpRequest):
    posts = []

    if "search" in request.GET:
        posts = Post.objects.filter(__name____contains=request.GET["search"])

    if "date" in request.GET and len(request.GET["date"]) > 4:
        first_date = date.fromisoformat(request.GET["date"])
        end_date = first_date + timedelta(days=1)
        posts = posts.filter(published_at__gte=first_date, published_at__lt=end_date)


    return render(request, "App/search_page.html", {"posts" : posts})







def all_posts_view(request: HttpRequest):

    if "cat" in request.GET:
        posts = Post.objects.filter(category=request.GET["cat"])
    else:
        posts = Post.objects.all()

    return render(request, "All/all_posts.html", {"posts" : posts, "categories" : Post.categories.choices, })




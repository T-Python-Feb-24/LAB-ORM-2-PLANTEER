
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from datetime import date,timedelta
import math
from .models import Post
from .models import Comment

def home_page(request: HttpRequest):


    plant = Post.objects.all()

    return render(request,"App/index.html",{"posts":plant})


def add_post_view(request:HttpRequest):
    if request.method=='POST':
        try:
            new_post=Post(Name=request.POST['Name'],
                        about=request.POST['about'],
                        used_for=request.POST['used_for'],
                        image = request.FILES.get('image', Post.image.field.default),
                        eidble = request.POST.get("eidble", False),
                        category= request.POST["category"]
                    )
            new_post.save()
            return redirect('App:home_page')

        except Exception as e:
            print(e)

    return render(request,'App/add_post.html',{"categories" : Post.categories.choices})








def post_detail_view(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        #comments = comments.objects.filter(post=post)
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
    

    return redirect("App:post_detail.html")











def posts_search_view(request):
    query = request.GET.get('search')
    if query:
    
        posts = Post.objects.filter(Name__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'App/posts_search.html', {'posts': posts})













def add_comment_view(request:HttpRequest, post_id):

    if request.method == "POST":
        #add new comment
        post_object = Post.objects.get(pk=post_id)
        new_comment = Comment(post=post_object,full_name=request.POST["full_name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("App:post_detail_view", post_id=post_id)
    













def all_posts_view(request: HttpRequest):

    if "cat" in request.GET:
        posts = Post.objects.filter(category=request.GET["cat"])
    else:
        posts = Post.objects.all()

    return render(request, "App/all_posts.html", {"posts" : posts, "categories" : Post.categories.choices, })




def add_comment_view(request:HttpRequest, post_id):

    if request.method == "POST":
        post_object = Post.objects.get(pk=post_id)
        new_comment = Comment(post=post_object,full_name=request.POST["full_name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("App:post_detail_view", post_id=post_object.id)




def contact_us_view(request):
    if request.method == 'POST':
        return HttpResponse('Message sent successfully! Thank you for contacting us.')
    else:
        return render(request, 'App/contact.html')
    
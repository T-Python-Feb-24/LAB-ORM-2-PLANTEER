from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#import User Model
from django.contrib.auth.models import User
#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout 
from main.models import Comment 
from .models import Profile
from django.db import transaction

# Create your views here.

def register_user_view(request:HttpRequest):
    if request.method == "POST":
        
        try:
            with transaction.atomic():
                if User.objects.filter(username=request.POST["username"]).exists():
                    msge=" Username already exite , try another username "
                    return render(request, "accounts/register.html",{"msge":msge})
                
                new_user = User.objects.create_user(username=request.POST["username"],
                email=request.POST["email"], first_name=request.POST["first_name"], 
                last_name=request.POST["last_name"], password=request.POST["password"]
                )
                
                new_user.save()

                profile = Profile(user=new_user, about=request.POST["about"], 
                instagram=request.POST["instagram"], 
                linkedin=request.POST["linkedin"],
                avatar=request.FILES.get("avatar", Profile.avatar.field.get_default()))
                profile.save()

             #redirect to login page
                return redirect("accounts:login_user_view")
        except Exception as e:
            print(e)
    
    return render(request, "accounts/register.html")






def login_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        #authenticat user
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            #login user
            login(request, user)
            return redirect("main:home")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "accounts/login.html", {"msg" : msg})


def logout_user_view(request:HttpRequest ):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user_view')


def user_info(request:HttpRequest , username):
    try:
        user=User.objects.get(pk=username)
        #user_comment=user.objects.comment_set.all()
        #user_comment=Comment.objects.filter(user=user)
        #user_information=User.objects.all()
    except:
        user=None

    return render(request, "accounts/user_info.html", {"user":user})



def update_info(request:HttpRequest , username):

    acc=User.objects.get(pk=username)
    info=Profile.objects.get(user=acc)
    if request.method == "POST":
        try:
            with transaction.atomic():
                acc.username=request.POST["username"]
                acc.first_name=request.POST["first_name"]
                acc.last_name=request.POST["last_name"]
                acc.email=request.POST["email"]
                acc.password=request.POST["password"]
                acc.save()
                info.about=request.POST["about"]
                info.instagram=request.POST["instagram"]
                info.linkedin=request.POST["linkedin"]
                info.avatar=request.FILES.get("avatar", info.avatar)
                info.save()
                return redirect("accounts:user_info_view", username=acc.id )
        except Exception as e:
            print(e)

    return render(request,'accounts/update_info.html' , {"acc" : acc ,"info":info })
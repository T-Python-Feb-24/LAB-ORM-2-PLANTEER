from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import transaction, IntegrityError
from .models import  ProfileUser


def register_user(request:HttpRequest):

 if request.method == "POST":
        
    try:
        with transaction.atomic():
      #create new user
            new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
            new_user.save()
            
            profile = ProfileUser(user=new_user, about=request.POST["about"], instagram_link=request.POST["instagram_link"], linked_link=request.POST["linked_link"], avatar=request.FILES.get("avatar", ProfileUser.avatar.field.get_default()))
            profile.save()

                #redirect to login page
            return redirect("accounts:login_user")
        
    except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

    except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

 return render(request,"accounts/register_user.html",)


def login_user(request:HttpRequest):
    msg = None

    if request.method == "POST":
        
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            
            login(request, user)
            return redirect("main:home_page")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "accounts/login_user.html", {"msg" : msg})


def logout_user(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user')


def profile(request:HttpRequest,username):
   
  profile=User.objects.get(username=username)
    
  return render(request,"accounts/profile.html",{'profile':profile})


def update_profile(request:HttpRequest):
    if request.method == "POST":
        
     try:
        
         new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
         new_user.save()

            #redirect to login page
         return redirect("accounts:profile")

     except Exception as e:
            print(e)
    

    return render(request,"main:not_found.html")

    
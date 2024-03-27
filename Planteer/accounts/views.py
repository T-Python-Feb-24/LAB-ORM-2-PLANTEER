from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#import User Model
from django.contrib.auth.models import User
#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from main.models import Comment
from .models import profile
#import transaction
from django.db import transaction, IntegrityError
# Create your views here.

def register_view(request:HttpRequest):
    msg=None
    if request.method =="POST":
        try:
         with transaction.atomic():
            new_account=User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                password=request.POST["password"]
                )
            new_account.save()
            new_profile= profile(user=new_account ,linkedin_link=request.POST["linkedin_link"],avatar=request.FILES.get("avatar", profile.avatar.field.get_default()))
            new_profile.save()
            return redirect("accounts:login_view")
        except IntegrityError:
           msg= "sorry the username with the same user , please choose a different username"
        except Exception as e:
          print(e)
    return render(request,"accounts/register.html", {"msg":msg})

def login_view(request:HttpRequest):
    
    msg=None

    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request,user)
            return redirect("main:home_view")
        else:
            msg="username or password not found ,try agin"
    return render(request,'accounts/login.html',{"msg":msg})

def logout_view(request:HttpRequest):
    if request.user.is_authenticated:
       logout(request)
    return redirect('accounts:login_view')

def profile_view(request:HttpRequest,user_name):
 user=User.objects.get(username= user_name)
 #username=user.username if request.user.is_authenticated else None
 #first_name=user.first_name if request.user.is_authenticated else None
 
 #last_name=user.last_name if request.user.is_authenticated else None
 #email=user.email if request.user.is_authenticated else None
 
 #email=request.POST.get["email"],
 #first_name=request.POST.get["first_name"],
 #last_name=request.POST.get["last_name"],
 return render(request,'accounts/profile.html', {"user":user})

def update_profile(request:HttpRequest,user_name):
    user = User.objects.get(username=user_name)

    if request.method == "POST":
        try:
            user.username = request.POST["username"]
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            user.email = request.POST["email"]
            user.password=request.POST["password"] 
           #profile.linkedin_link= request.Post["linkedin_link"]
            user.save()
            return redirect("accounts:profile_niew", {"user":user})
        except Exception as e:
            print(e)
    return render(request,"accounts/update.html")
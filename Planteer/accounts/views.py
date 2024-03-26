from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

def register_view(request:HttpRequest):
    msg=None
    if request.method =="POST":
        try:
            new_account=User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                password=request.POST["password"]
                )
            new_account.save()
           # if messages.success:
             #msg="accounts created successfully. please login in"
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

def profile_view(request:HttpRequest):
 user=request.user
 username=user.username if request.user.is_authenticated else None
 first_name=user.first_name if request.user.is_authenticated else None
 last_name=user.last_name if request.user.is_authenticated else None
 email=user.email if request.user.is_authenticated else None
 
 #email=request.POST.get["email"],
 #first_name=request.POST.get["first_name"],
 #last_name=request.POST.get["last_name"],
 return render(request,'accounts/profile.html', {"user":user,"username":username ,"first_name":first_name ,"last_name":last_name ,"email":email})
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
from django.db import IntegrityError
# Create your views here.


def create_account (request :HttpRequest):
    # in case if we don't have exeption, it will be empty 
    msg=''
    
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                password = request.POST["password"]
            )
            user.save()
            return redirect("accounts:user_login")

        except IntegrityError:
            msg = "username already exists! Try with different username!"
        except Exception as e:
            print(e)
     
    return render(request,"accounts/create_account.html" ,{"msg":msg})


def user_login (request : HttpRequest):
    
    if request.method == "POST":
       user = authenticate(
           username=request.POST["username"],
           password=request.POST["password"]
           )
       # returns None if the credentials aren’t valid 
       if user is not None:
           login(request,user) 
           return redirect("main:home_page")
       else:
           pass 
    return render (request,"accounts/login.html")


def user_logout(request : HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect("main:home_page")


def user_profile (request: HttpRequest):
    # create object , get with username + <> 
    return render(request,"accounts/user_profile.html")


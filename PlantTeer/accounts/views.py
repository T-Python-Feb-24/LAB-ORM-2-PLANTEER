from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_user(request:HttpRequest):

    if request.method == "POST":
        
        try:
            #create new user
            new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
            new_user.save()

            #redirect to login page
            return redirect("accounts:login_user")

        except Exception as e:
            print(e)
    

    return render(request,"accounts/register_user.html")


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

def profile(request:HttpRequest):
    return render("accounts:profile")
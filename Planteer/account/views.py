from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#import User Model
from django.contrib.auth.models import User
#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.

def register_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:


            #create new user
            new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
            new_user.save()

            #redirect to login page
            return redirect("accounts:login_user_view")
        
        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "account/register.html", {"msg" : msg})


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
    

    return render(request, "account/login.html", {"msg" : msg})


def logout_user_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('account:login_user_view')



def user_profile_view(request:HttpRequest, user_name):

    try:
        user_info = User.objects.get(username=user_name)
    except:
        return render(request, "main/not_found.html")

    return render(request, "account/profile.html", {"user_info":user_info})
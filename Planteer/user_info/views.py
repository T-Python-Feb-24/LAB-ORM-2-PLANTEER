from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#import User Model
from django.contrib.auth.models import User
#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

def user_detail(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user_info/user_detail.html', {'user': user})

def register_user(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            new_user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                password=request.POST["password"]
            )
            new_user.save()
            # Redirect to login page
            return redirect("user_info:user_login")
        except IntegrityError:
            msg = "Username already exists. Please choose a different username."

    return render(request, "user_info/register.html", {"msg": msg})



def user_login(request:HttpRequest):
    msg = None

    if request.method == "POST":
        #authenticat user
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            #login user
            login(request, user)
            return redirect("home")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "user_info/login.html", {"msg" : msg})


def user_logout(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('user_info:user_login')
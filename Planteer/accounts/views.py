from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#import User Model
from django.contrib.auth.models import User
#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout


def register_user_view(request:HttpRequest):
    if request.method == "POST":
        try:
            #create user
            user = User.objects.create_user(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            user.save()
            return redirect("accounts:login_user_view")
        except Exception as e:
            print(e)
    return render(request, "accounts/register_user.html")

def login_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if user:
            login(request, user)
            return redirect("plants:index_view")
        else:
            msg = "Username or password is not correct!!. Try again..."
    return render(request, "accounts/login_user.html", {"msg" : msg})


def logout_user_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user_view')


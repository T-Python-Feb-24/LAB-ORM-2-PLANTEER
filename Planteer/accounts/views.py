from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def register_user(request:HttpRequest):

    if request.method == 'POST':
        try:
            new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
            new_user.save()
            return redirect("accounts:login_user")
        except Exception as e:
            print(e)

    return render(request, "register.html")



def login_user(request:HttpRequest):
    message = None

    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user :
            login(request,user)
            return redirect('main:home_page')
        else:
            message = "Username or Password is wrong. Please try again."

    return render(request, "login.html", {"message" : message})



def logout_user(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user')
from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

def register_user(request: HttpRequest):
    if request.method == "POST":
        try:
            new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
            new_user.save()
            return redirect("accounts:login_user")
        except IntegrityError:  
            error_message = "try to sign up with a username that already exist."
            return render(request, "accounts/register.html", {"error_message": error_message})
    return render(request, "accounts/register.html")
def login_user(request:HttpRequest):
    msg = None

    if request.method == "POST":
       
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            
            login(request, user)
            return redirect("main:home")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "accounts/login.html", {"msg" : msg})

 

def logout_user(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user')

def user_detail(request, username):
    
    user = get_object_or_404(User, username=username)
    
    
    
    return render(request, 'accounts/detail_page.html', {'user': user})

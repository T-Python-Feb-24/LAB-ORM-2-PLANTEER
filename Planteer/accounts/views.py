from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError

# Create your views here.

def register_page(request: HttpRequest):
    if request.method == "POST":
        try:
            new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
            new_user.save()
            return redirect("accounts:login_page")
        except IntegrityError: 
            error_message = "try to sign up with a username that already exists."
            return render(request, "accounts/register_page.html", {"error_message": error_message})
    return render(request,"accounts/register_page.html")

def login_page(request:HttpRequest):
    msg= None
    if request.method == "POST":
        user=authenticate(request,username=request.POST["username"],password=request.POST["password"])

        if user:
            login(request,user)
            return redirect("main:index_page")
        else:
            msg="Username or password is worng."
    return render(request,"accounts/login_page.html",{"msg":msg})


def logout_user_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)

    return redirect("main:index_page")


def user_profile(request:HttpRequest, username):
    user= get_object_or_404(User,username=username)
    return render(request,"accounts/user_profile.html",{"user":user})
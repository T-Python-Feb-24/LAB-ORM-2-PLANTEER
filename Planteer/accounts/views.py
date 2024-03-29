from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
from django.db import IntegrityError
from .models import Profile
from django.db import transaction

# Create your views here.


def create_account (request :HttpRequest):
    msg=""
    
    if request.method == "POST":
        try:
            
            with transaction.atomic():
                user = User.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["email"],
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    password = request.POST["password"]
                )
                user.save()
                
                profile = Profile(
                    user = user,
                    about = request.POST["about"],
                    avatar = request.FILES.get("avatar"),
                    twitter = request.POST["twitter"],
                    linkedin = request.POST["linkedin"]
                )
                profile.save() 

            return redirect("accounts:user_login",{"profile":profile})

        except IntegrityError:
            msg = "username already exists! Try with different username!"
        except Exception as e:
            msg=f"something went wrong, {e}"
     
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


def user_profile (request: HttpRequest,username):

    user= User.objects.get(username = username)
    
    return render(request,"accounts/user_profile.html",{"user":user})


def update_profile(request : HttpRequest, username):
    
    msg= None
    
    if not request.user.is_authenticated:
        return redirect("accounts:user_login")
   
    if request.method == "POST":
    
        try:
        
            with transaction.atomic():
                user:User = request.user 
            
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            user.email = request.POST["email"]
            user.save()
         
            try:
                profile:Profile = user.profile
            except Exception as e:
                profile = Profile(user=user) 
                
            profile.about = request.POST["about"]
            profile.avatar = request.FILES.get("avatar",profile.avatar)
            profile.twitter = request.POST["twitter"]
            profile.linkedin = request.POST["linkedin"]
            profile.save()
        
            return redirect("accounts:user_profile", username=user.username)
        
        except Exception as e:
            msg = f"Something went wrong {e}"
            print(e)
    
    return render(request ,"accounts/update_profile.html", {"msg":msg})

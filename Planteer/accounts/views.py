from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction

# from main.models import Comment
from .models import Profile


def register_user_view(request:HttpRequest):
    message = None

    if request.method == "POST":
        
        try:
            # if User.objects.filter(username=request.POST['username']).exists():
            #     msg = "Username is already exist. Please choose another one."
            #     return render(request, "accounts/register.html", {"message" :msg})
            
            with transaction.atomic():
                #create new user
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                #create profile for user
                profile = Profile(user=new_user, about=request.POST["about"], instagram_link=request.POST["instagram_link"], linked_link=request.POST["linked_link"], avatar=request.FILES.get("avatar", Profile.avatar.field.get_default()))
                profile.save()

                #redirect to login page
                return redirect("accounts:login")
        except IntegrityError as e:
            message = "Username is already exist. Please choose another one."
            print(e)

        except Exception as e:
            message = "Something went wrong. Please try again."
            print(e)

    return render(request, "accounts/register.html", {"message": message})

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
    

    return render(request, "accounts/login.html", {"msg" : msg})

def logout_user_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login')

def profile_view(request:HttpRequest, user_name):
    # if request.user.is_authenticated:
    #     user = request.user
    #     first_name = user.first_name
    #     last_name = user.last_name
    #     email = user.email
    #     username = user.username

    #     context = {"first_name": first_name, "last_name": last_name, "email": email, "username": username}
        
    #     return render(request, 'accounts/profile.html', context)
    # else:
    #     return redirect("accounts:login")

    try:
        user_info = User.objects.get(username = user_name)
    except:
        return render(request, "404.html")
    
    return render(request, "accounts/profile.html", {"user_info": user_info})

def update_user(request: HttpRequest, user_name):
    message = None

    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    try:
        user_info = User.objects.get(username = user_name)
    except:
        return render(request, "404.html")
    
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
                profile.instagram_link = request.POST["instagram_link"]
                profile.linked_link = request.POST["linked_link"]
                profile.avatar = request.FILES.get("avatar", profile.avatar)

                profile.save()

                return redirect("accounts:profile", user_name=user.username)

        except Exception as e:
            message = f"Something went wrong {e}"
            print(e)

    return render(request, "accounts/update_profile.html", {"user_info": user_info ,"message" : message})
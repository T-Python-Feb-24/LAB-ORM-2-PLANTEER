from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from App.models import Comment

from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db import transaction, IntegrityError




def register_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        
        try:
            with transaction.atomic():

                 new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"],
                 last_name=request.POST["last_name"], password=request.POST["password"])
                 new_user.save()
                 profile = Profile(user=new_user, about=request.POST["about"], instagram_link=request.POST["instagram_link"], linked_link=request.POST["linked_link"], avatar=request.FILES.get("avatar", Profile.avatar.field.get_default(), birth_date = redirect.POST["birth_date"]))
                 profile.save()
                                               


            

        
            return redirect("user_name:login_user_view")

        except Exception as e:
            msg ="USERNAME ALREADY EXISTS.PLEASE CHOOSE A DIFFERENT USERNAME"
            print(e)
        except Exception as e:
            msg ="SOMETHING WENT WRONG .PLEASE TRY AGAIN"
    

    return render(request, "user_name/register.html")


def login_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
        
            login(request, user)
            return redirect("App:home_page")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "user_name/login.html", {"msg" : msg})


def logout_user_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('user_name:login_user_view')


def user_profile_view(request:HttpRequest, user_name):

    try:
        user_info = User.objects.get(username=user_name)
        user_comments = user_info.comment_set.all() 


    except:
        return render(request, "App/not_found.html")

    return render(request, "user_name/profile.html", {"user_info":user_info,'comments':user_comments})




def update_profile_view(request:HttpRequest):
    msg = None

    if not request.user.is_authenticated:
        return redirect("user_name:login_user_view")
    
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

                return redirect("user_name:user_profile_view", user_name=user.username)

        except Exception as e:
            msg = f"Something went wrong {e}"
            print(e)

    return render(request, "user_name/update.html", {"msg" : msg})


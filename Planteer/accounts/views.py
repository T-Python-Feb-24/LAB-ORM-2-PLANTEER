from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#import User Model
from django.contrib.auth.models import User
#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from plants.models import Comment
from .models import Profile
#import transaction
from django.db import transaction, IntegrityError




def register_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:

            #using transaction to ensure all operations are successfull
            with transaction.atomic():
                #create user
                user = User.objects.create_user(
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    username=request.POST["username"],
                    email=request.POST["email"],
                    password=request.POST["password"],
                )
                user.save()

                profile = Profile(
                    # userObject from profile model = user 
                    user = user,
                    about = request.POST["about"],
                    instagram_link=request.POST["instagram_link"], 
                    linked_link=request.POST["linked_link"], 
                    avatar=request.FILES.get("avatar", Profile.avatar.field.get_default())
                )
                profile.save()

            return redirect("accounts:login_user_view")
        
        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

        except Exception as e:
            print(e)
    return render(request, "accounts/register_user.html", {"msg" : msg})

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

def user_profile_view(request:HttpRequest, user_name):

    try:
        user_key = User.objects.get(username=user_name)
    except:
        user_key = None # notfound page  

    return render(request, "accounts/user_profile.html", {"user_key" : user_key})


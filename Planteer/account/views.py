from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#import User Model
from django.contrib.auth.models import User
#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from main.models import Comment
from .models import Profile
#import transaction
from django.db import transaction, IntegrityError


# Create your views here.

def register_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:

            #using transaction to ensure all operations are successfull
            with transaction.atomic():
                #create new user
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                #create profile for user
                profile = Profile(user=new_user, about=request.POST["about"], instagram_link=request.POST["instagram_link"], linked_link=request.POST["linked_link"], avatar=request.FILES.get("avatar", Profile.avatar.field.get_default()))
                profile.save()

                #redirect to login page
                return redirect("account:login_user_view")
        
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
        user_object = User.objects.get(username=user_name)
        #comment by this user
        #user_comments = Comment.objects.filter(user=user_object)
        #user_comments = user_object.comment_set.all() #using set
    except:
        return render(request, "main/not_found.html")

    return render(request, "account/profile.html", {"user_object":user_object})
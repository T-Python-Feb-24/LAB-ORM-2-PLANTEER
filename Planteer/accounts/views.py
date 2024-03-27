from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.db import transaction, IntegrityError
from .models import Profile


# Create your views here.

def register_page(request: HttpRequest):
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
                return redirect("accounts:login_page")
        
        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "accounts/register_page.html", {"msg" : msg})


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





def user_profile(request: HttpRequest, username):
    user = get_object_or_404(User, username=username)
    msg = None
    
    if request.method == "POST" and request.user == user:
        try:
            new_username = request.POST.get("username")
            new_first_name = request.POST.get("first_name")
            new_last_name = request.POST.get("last_name")

            # Check if the new username is available and not taken by another user
            if new_username != user.username and User.objects.filter(username=new_username).exists():
                msg = "Username already exists. Please choose a different username."
            else:
                user.username = new_username
                user.first_name = new_first_name
                user.last_name = new_last_name
                user.save()

                profile = user.profile
                profile.about = request.POST.get("about")
                profile.instagram_link = request.POST.get("instagram_link")
                profile.linkedin_link = request.POST.get("linkedin_link")

                if "avatar" in request.FILES:
                    profile.avatar = request.FILES["avatar"]

                profile.save()

                # Update email if provided
                new_email = request.POST.get("email")
                if new_email:
                    user.email = new_email
                    user.save()

                msg = "Profile updated successfully."

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)

    return render(request, "accounts/user_profile.html", {"user": user, "msg": msg})
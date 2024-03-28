from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Profile
from django.contrib import messages

from django.db import transaction, IntegrityError



def register_user_view(request:HttpRequest):

    msg = None
    
    if request.method == "POST":
        try:

            with transaction.atomic():
                #create new user
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                #create profile for user
                profile = Profile(user=new_user, about=request.POST["about"], avatar=request.FILES.get("avatar", Profile.avatar.field.get_default()))
                profile.save()

                #redirect to login page
                return redirect("accounts:login_user_view")

        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)


    return render(request, "accounts/register.html", {"msg" : msg})

def login_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        #authenticat user
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            #login user
            login(request, user)
            return redirect("main:home_view")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "accounts/login.html", {"msg" : msg})


def logout_user_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user_view')

def user_detail_view(request:HttpRequest, user_id):

    try:
        user = User.objects.get(pk=user_id)

    except User.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)

    return render(request, "accounts/detail.html", {"user":user})

@login_required

def update_profile_view(request:HttpRequest):

    if request.method == 'POST':
        about = request.POST.get('about')
        avatar = request.FILES.get('avatar')


        profile = request.user.profile
        profile.about = about
        if avatar:
            profile.avatar = avatar
            profile.save()


            messages.success(request, 'Your profile has been updated successfully!')

        return render(request, 'accounts/detail.html')  
    else:
        return render(request, 'accounts/update_profile.html')
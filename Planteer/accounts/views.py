from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Profile
from django.contrib import messages

from django.db import transaction, IntegrityError

def register_user(request: HttpRequest):
    
    msg = None

    if request.method == "POST":
        try:

            with transaction.atomic():
                #create new user
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                #create profile for user
                profile = Profile(user=new_user, about=request.POST["about"], instagram_link=request.POST["instagram_link"], linked_link=request.POST["linkedin_link"], avatar=request.FILES.get("avatar", Profile.avatar.field.get_default()))
                profile.save()

                #redirect to login page
                return redirect("accounts:login_user")
        
        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "accounts/register.html", {"msg" : msg})



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

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        about = request.POST.get('about')
        instagram_link = request.POST.get('instagram_link')
        linkedin_link = request.POST.get('linkedin_link')
        avatar = request.FILES.get('avatar')
        
        
        profile = request.user.profile
        profile.about = about
        profile.instagram_link = instagram_link
        profile.linkedin_link = linkedin_link
        if avatar:
            profile.avatar = avatar
        profile.save()

        
        messages.success(request, 'Your profile has been updated successfully!')
        
        return render(request, 'accounts/profile_update.html')  
    else:
        return render(request, 'accounts/profile_update.html')
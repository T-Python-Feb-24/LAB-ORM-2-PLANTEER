from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.db import IntegrityError

def register_user_view(request:HttpRequest):
    msg = None
    
    if request.method == "POST":
        try:
            new_user = User.objects.create_user(username=request.POST["username"], 
                                                email=request.POST["email"], 
                                                first_name=request.POST["first_name"], 
                                                last_name=request.POST["last_name"], 
                                                password=request.POST["password"])
            new_user.save()

            return redirect("accounts:login_user_view")
        except IntegrityError:
                return render(request, "accounts/register.html", {'error': 'Username already exists.'})
        except Exception as e:
            print(e)

    return render(request, "accounts/register.html")

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
        return render(request, "accounts/account_not_found.html")
    except Exception as e:
        print(e)

    return render(request, "accounts/detail.html")
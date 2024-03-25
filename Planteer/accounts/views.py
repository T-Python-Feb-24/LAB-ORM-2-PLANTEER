from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

#import User Model
from django.contrib.auth.models import User

#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout

#For the duplicate username
from django.db import IntegrityError

# Create your views here.
def sign_up_view(request:HttpRequest):
    if request.method == 'POST':
        try:
            #create a new user
            new_user = User.objects.create_user(
                username = request.POST['username'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = request.POST['password']
            )
            new_user.save()
            return redirect('accounts:login_view')
        except IntegrityError:
            return render(request, 'accounts/sign_up.html', {'error': 'Username already exists'})
        except Exception as e:
            print(e)
    return render(request,'accounts/sign_up.html')

def login_view(request:HttpRequest):
    #the message will appear if the user enter wrong data
    msg = None

    if request.method == 'POST':

        #Authenticate the user by username and password
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        #this is means if user exist    
        if user:
            login(request, user)
            return redirect('main:index_view')
        else:
            msg = "Username or Password is wrong, Please try Again!!"
    
    return render(request, 'accounts/login.html', {"msg" : msg})

def logout_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_view')

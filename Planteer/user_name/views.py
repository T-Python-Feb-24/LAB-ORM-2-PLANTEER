from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User


def register_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home_page')  # Redirect to the home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'App/register.html', {'form': form})




def login_user_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'App/login.html', {'form': form})



def logout_user_view(request):
    (request)
    return redirect('home_page')  # Redirect to the home page after logout





def user_detail_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'App/user_detail.html', {'user': user})

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model


def sign_up_view(request: HttpRequest):
    try:
        msg = None
        if request.method == "POST":

            username = request.POST.get("username")
            email = request.POST.get("email")
            if not (get_user_model().objects.filter(username=username).exists()
                    or get_user_model().objects.filter(email=email).exists()):

                # create new user
                new_user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    password=request.POST.get("password")
                )
                new_user.save()

                # redirect to login page
                return redirect("account:login_view")
            else:
                msg = "Username or Email already exist. Try again..."

    except Exception as e:
        print(e)

    return render(request, "account/sign_up.html", {"msg": msg})


def login_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        # authenticat user
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user:
            # login user
            login(request, user)
            return redirect("main:index_view")
        else:
            msg = "Username or Password is wrong. Try again..."

    return render(request, "account/login.html", {"msg": msg})


def logout_view(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main:index_view')


def user_profile_view(request: HttpRequest, user_name):
    try:
        msg = None
        user = get_user_model().objects.get(username=user_name)
    except User.DoesNotExist:
        msg = "User Not Found"
        return render(request, "account/user_profile.html", {"msg": msg})
    return render(request, "account/user_profile.html", {"user": user})


def profiles_view(request: HttpRequest):
    try:
        msg = None
        users = get_user_model().objects.all()
    except User.DoesNotExist:
        msg = "No Users Found"
        return render(request, "account/profile.html", {"msg": msg})

    return render(request, "account/profile.html", {"users": users})

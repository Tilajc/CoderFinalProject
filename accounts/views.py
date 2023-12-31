from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm, UpdateForm, AvatarUpdateForm
from accounts.models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

        return redirect('Profile')

    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("Login")

    form = SignUpForm()

    context = {"form": form}

    return render(request, "accounts/signup.html", context)
@login_required
def update(request):
    user = request.user

    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            user.email = request.POST["email"]
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]

            user.save()
            return redirect("Profile")

    form = UpdateForm(initial={"username": user.username, "email": user.email, "first_name": user.first_name, "last_name": user.last_name})

    context = {
        "form": form,
        "page": 'update'
    }

    return render(request, "accounts/signup.html", context)

@login_required
def profile(request):
    user = request.user

    context = {
        "user": user
    }
    return render(request, "accounts/profile.html", context)

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return render(request, "accounts/deleted.html")

@login_required
def update_avatar(request):
    user= request.user
    if request.method == "POST":
        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.IMG = data["IMG"]
            except:
                avatar = Avatar(
                    user=user,
                    IMG=data["IMG"]
                )

            avatar.save()
            return redirect("Profile")

    form = AvatarUpdateForm()
    context = {"form": form}
    return render(request, "accounts/avatar.html", context)
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm, UpdateForm


def login(request):
    return render(request, "accounts/login.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("Login")

    form = SignUpForm()

    context = {"form": form}

    return render(request, "accounts/signup.html", context)

def update(request):
    user = request.user

    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            user.email = request.POST["email"]
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]

            user.save()
            return redirect("Home")

    form = UpdateForm(initial={"username": user.username, "email": user.email, "first_name": user.first_name, "last_name": user.last_name})

    context = {
        "form": form
    }

    return render(request, "accounts/signup.html", context)
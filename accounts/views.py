from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


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
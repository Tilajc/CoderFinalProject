from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


def login(request):
    return render(request, "accounts/login.html")

def signup(request):

    form = SignUpForm()

    return render(request, "accounts/signup.html")
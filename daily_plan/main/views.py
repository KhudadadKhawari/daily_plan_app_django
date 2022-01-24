from django.shortcuts import render, HttpResponse
from django.template import context

# Create your views here.

def home(request):
    context={
        'active_nav': 'home',
    }
    return render(request, "main/home.html", context)


def user_register(request):
    return render(request, "main/register.html")


def user_login(request):
    return render(request, 'main/user_login.html')


def user_profile(request):
    context={
        'active_nav': 'profile',
    }
    return render(request, 'main/user_profile.html', context)


def archive(request):
    context={
        'active_nav': 'archive',
    }
    return render(request, 'main/archive.html', context)

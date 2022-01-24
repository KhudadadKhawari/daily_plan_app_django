from django.shortcuts import render, redirect
from .models import Plan
from django.contrib.auth.models import User
from .forms import  PlanForm, UserCreateForm
from django.contrib import messages
# Create your views here.

def home(request):
    today_plans = Plan.objects.all()
    print(today_plans)
    context={
        'active_nav': 'home',
        'today_plans':today_plans
    }
    return render(request, "main/home.html", context)


def user_register(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username').lower()
            user.save()
            messages.success(request, "Account Created Successfully!!!", "alert-success")
            return redirect('home')
        else:
            messages.info(request, "User not created, Error", 'alert-info')
    context={
        'form': form,
    }
    return render(request, "main/register.html", context)


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

import imp
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.template import context
from .models import Plan
from django.contrib.auth.models import User
from .forms import  PlanForm, UserCreateForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from datetime import date
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

@login_required
def home(request):
    user = request.user
    today = date.today()
    today_plans = Plan.objects.filter(user=user, date_created=today).order_by('-id')
    if request.method =='POST':
        new_plan = request.POST.get('new_plan')
        Plan.objects.create(
            description=new_plan,
            user=user
        )
    context={
        'active_nav': 'home',
        'today_plans':today_plans
    }
    return render(request, "main/home.html", context)


@unauthenticated_user
def user_register(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        try:
            if form.is_valid():
                user = form.save(commit=False)
                user.username = form.cleaned_data.get('username').lower()
                user.save()
                messages.success(request, "Account Created Successfully!!!", "alert-success")
                return redirect('home')
            else:
                messages.info(request, "User not created, Error", 'alert-info')
        except IntegrityError as error:
            messages.info(request, f"A user with this username or email already exists", 'alert-info')
    context={
        'form': form,
    }
    return render(request, "main/register.html", context)

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is Incorrect", 'alert-danger')
            return redirect('user_login')
    return render(request, "main/user_login.html")


def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required
def change_password(request):
    user = request.user
    form = PasswordChangeForm(user)
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Changed Successfully", "alert-success")
            return redirect('change_password')
    context={
        'form':form,
        'active_nav':'change_password',
    }
    return render(request, 'main/change_password.html', context)

@login_required
def user_profile(request):
    user = request.user
    form = UserProfileForm(instance=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            the_user = form.save(commit=False)
            the_user.username = form.cleaned_data.get('username').lower()
            the_user.save()
            messages.success(request, "Profile Details Updated Successfully", "alert-success")
            return redirect('user_profile')
    context={
        'active_nav': 'profile',
        'form':form,
    }
    return render(request, 'main/user_profile.html', context)


@login_required
def archive(request):
    user = request.user
    today = date.today()
    plans = Plan.objects.filter( user=user)
    # ~Q(date_created=today)
    context={
        'active_nav': 'archive',
        'plans': plans,
    }
    return render(request, 'main/archive.html', context)


@login_required
def complete_plan(request, id):
    user = request.user
    plan = Plan.objects.get(id=id, user=user)
    if request.method == "POST":
        plan.status = 1
        plan.save()
    return redirect('home')


@login_required
def update_plan(request, id):
    user = request.user
    plan = Plan.objects.get(id=id, user=user)
    if request.method == "POST":
        new_description = request.POST.get('update_plan')
        plan.description = new_description
        plan.save()
        messages.info(request, "Plane Descriptions Updated Successfully", 'alert-success')
    return redirect('home')


@login_required
def update_plan(request, id):
    user = request.user
    plan = Plan.objects.get(id=id, user=user)
    if request.method == "POST":
        new_description = request.POST.get('update_plan')
        plan.description = new_description
        plan.save()
        messages.info(request, "Plane Descriptions Updated Successfully", 'alert-success')
    return redirect('home')


@login_required
def delete_plan(request, id):
    user = request.user
    plan = Plan.objects.get(id=id, user=user)
    redirect_view = request.GET.get('redirect_view','home')
    if request.method == "POST":
        plan.delete()
        messages.info(request, "Plan Deleted", 'alert-info')
    return redirect(redirect_view)
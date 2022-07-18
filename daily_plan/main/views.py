from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Archive, EducationalNote, PersonalNote, BusinessNote
from .forms import   UserCreateForm, UserProfileForm
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
    educational_notes = EducationalNote.objects.filter(user=user, date_created__year=today.year, date_created__month=today.month, date_created__day=today.day)
    personal_notes = PersonalNote.objects.filter(user=user, date_created__year=today.year, date_created__month=today.month, date_created__day=today.day)
    business_notes = BusinessNote.objects.filter(user=user, date_created__year=today.year, date_created__month=today.month, date_created__day=today.day)

    if request.method =='POST':
        try:
            title = request.POST['title']
            description = request.POST['description']
            category = request.POST['category']
            if category == 'educational_note':
                note = EducationalNote(user=user, title=title, description=description)
                note.save()
                messages.success(request, 'Educational note added successfully', 'alert alert-success')
                return redirect('home')
            elif category == 'personal_note':
                note = PersonalNote(user=user, title=title, description=description)
                note.save()
                messages.success(request, 'Personal note added successfully', 'alert alert-success')
                return redirect('home')
            elif category == 'business_note':
                note = BusinessNote(user=user, title=title, description=description)
                note.save()
                messages.success(request, 'Business note added successfully', 'alert alert-success')
                return redirect('home')
        except Exception as e:
            messages.error(request, 'Error: ' + str(e), 'alert alert-danger')
            return redirect('home')

    context={
        'active_nav': 'home',
        'personal_notes': personal_notes,
        'educational_notes': educational_notes,
        'business_notes': business_notes,
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
    notes = Archive.objects.all().filter(user=user).order_by('-id')
    context={
        'active_nav': 'archive',
        'notes': notes,
    }
    return render(request, 'main/archive.html', context)



@login_required
def update_note(request, category, id):
    try:
        if category == 'educational_note':
            note = EducationalNote.objects.get(id=id)
        elif category == 'personal_note':
            note = PersonalNote.objects.get(id=id)
        elif category == 'business_note':
            note = BusinessNote.objects.get(id=id)
        else:
            messages.error(request, "Error: Note Category Not found", 'alert-danger')
            return redirect('home')
        if request.method == "POST" and note.user == request.user:
            note.title = request.POST['title']
            note.description = request.POST['description']
            note.save()
            messages.info(request, "Notee Descriptions Updated Successfully", 'alert-success')
        else:
            messages.error(request, "Error: You are not authorized to update this note", 'alert-danger')
        return redirect('home')
    except Exception as e:
        messages.error(request, "Error: " + str(e), 'alert-danger')
        return redirect('home')


@login_required
def delete_note(request,category, id):
    user = request.user
    try:
        if category == 'educational_note':
            note = EducationalNote.objects.get(id=id)
        elif category == 'personal_note':
            note = PersonalNote.objects.get(id=id)
        elif category == 'business_note':
            note = BusinessNote.objects.get(id=id)
        else:
            messages.error(request, "Error: Note Category Not found", 'alert-danger')
            return redirect('home')
        if note.user == user:
            archived = Archive(user=user, title=note.title, description=note.description, category=category)
            archived.save()
            note.delete()
            messages.info(request, "Note Deleted and Archived Successfully", 'alert-success')
            return redirect ('home')
        
    except Exception as e:
        messages.error(request, "Error: " + str(e), 'alert-danger')
        return redirect('home')
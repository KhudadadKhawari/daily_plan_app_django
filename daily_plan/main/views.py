from django.shortcuts import render, HttpResponse
from django.template import context

# Create your views here.

def home(request):
    context={
        'number':234523452345,
        'text': 'Mr merwais',
    }
    return render(request, "main/home.html", context)


def user_register(request):
    return render(request, "main/register.html")


def user_login(request):
    return render(request, 'main/user_login.html')
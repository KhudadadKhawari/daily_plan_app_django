"""daily_plan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('register/', views.user_register, name='user_register' ),
    path('accounts/login/', views.user_login, name='user_login' ),
    path('accounts/logout/', views.user_logout, name='user_logout' ),
    path('accounts/change_password/', views.change_password, name='change_password' ),
    path('profile/', views.user_profile, name='user_profile' ),
    path('archive/', views.archive, name='archive' ),
    path('plan/<str:id>/complete/', views.complete_plan, name='complete_plan' ),
    path('plan/<str:id>/update/', views.update_plan, name='update_plan' ),
    path('plan/<str:id>/delete/', views.delete_plan, name='delete_plan' ),
]

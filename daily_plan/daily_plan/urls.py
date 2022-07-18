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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('register/', views.user_register, name='user_register' ),
    path('accounts/login/', views.user_login, name='user_login' ),
    path('accounts/logout/', views.user_logout, name='user_logout' ),
    path('accounts/change_password/', views.change_password, name='change_password' ),
    path('profile/', views.user_profile, name='user_profile' ),
    path('archive/', views.archive, name='archive' ),
    path('note/<category>/<id>/update/', views.update_note, name='update_note' ),
    path('note/<category>/<id>/delete/', views.delete_note, name='delete_note' ),

    # Forget Password
    path('account/password_reset/', auth_views.PasswordResetView.as_view(template_name='main/forgot_password/password_reset.html'), name='password_reset'),
    path('account/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/forgot_password/password_reset_done.html'), name='password_reset_done'),
    path('account/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/forgot_password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('account/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/forgot_password/password_reset_complete.html'), name='password_reset_complete'),
]

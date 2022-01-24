from django import forms
from django.forms import ModelForm
from .models import Plan
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Username',}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'First Name',}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Last Name',}),
            'email': forms.EmailInput(attrs={'class':'form-control form-control-user', 'placeholder':'Email',}),
            # 'password1': forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Password', 'name':'password', 'id':'password'}),
            # 'password2': forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Confirm_password', 'name':'Confirm_password', 'id':'Confirm_password'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Password','onkeyup':'check();'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Confirm Password','onkeyup':'check();'})

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data
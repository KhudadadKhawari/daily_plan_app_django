from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Username',}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'First Name',}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Last Name',}),
            'email': forms.EmailInput(attrs={'class':'form-control form-control-user', 'placeholder':'Email',}),
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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']
        widgets ={
            'username': forms.TextInput(attrs={'class':'form-control ', 'id':'username', 'placeholder':'Username',}),
            'first_name': forms.TextInput(attrs={'class':'form-control ', 'id':'first_name', 'placeholder':'First Name',}),
            'last_name': forms.TextInput(attrs={'class':'form-control ', 'id':'last_name', 'placeholder':'Last Name',}),
            'email': forms.EmailInput(attrs={'class':'form-control ', 'id':'email', 'placeholder':'Email','readonly':'true'}),
        }


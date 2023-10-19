from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label= 'Password', widget= forms.PasswordInput)
    password2= forms.CharField(label= 'Password confirmation', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts= {k: '' for k in fields}

class UserEditForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label= 'Password', widget= forms.PasswordInput)
    password2= forms.CharField(label= 'Password confirmation', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ['email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts= {k: '' for k in fields}
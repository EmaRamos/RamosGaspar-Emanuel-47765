from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *

# Create your views here.

def login_request(request):
    
    if request.method == 'POST':

        form= AuthenticationForm(request, data= request.POST)

        if form.is_valid():

            u= form.cleaned_data.get('username')
            p= form.cleaned_data.get('password')

            user= authenticate(username= u, password= p)

            if user is not None:
                
                login(request, user)
                
                messages.success(request, ('¡You have been logged in!'))

                return redirect('Home')
        
        else:

            messages.success(request, ('¡There was an error! Please try again.'))
            
            return redirect('Home')
    
    else:

        form= AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def register(request):

      if request.method == 'POST':

            form= UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username= form.cleaned_data['username']
                  
                  form.save()

                  messages.success(request, (f'User created successfully.'))
                  
                  return redirect('Home')

      else:
                   
            form= UserRegisterForm()     

      return render(request, 'accounts/register.html',  {'form': form})

@login_required
def edit_user(request):
    
    user= request.user

    if request.method == 'POST':
        
        form= UserEditForm(request.POST)
          
        if form.is_valid():
            
            info= form.cleaned_data

            user.email= info['email']
            user.set_password(info['password1'])
            user.first_name= info['first_name']
            user.last_name= info['last_name']
            user.email= info['email']

            user.save()

            messages.success(request, (f'User modified successfully.'))

            return redirect('Home')
          
    else:

        form= UserEditForm(initial= {
             'email': user.email,
             'first_name': user.first_name,
             'last_name': user.last_name,

        })

    return render(request, 'accounts/edit.html', {'form': form, 'user': user})

@login_required
def logout_request(request):
    
    logout(request)

    messages.success(request, (f'Logout sucessfully.'))
    
    return redirect('Home')
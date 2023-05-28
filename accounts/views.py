from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registration/signup.html', {
                            'form': UserCreationForm,
                            'error': 'Username already exists'
                            })
        else:
            return render(request, 'registration/signup.html', {
                        'form': UserCreationForm,
                        'error': 'Passwords does not match'
                   })


    else:
        return render(request, 'registration/signup.html', {
            'form': UserCreationForm
            })

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/signin.html', {
                        'form':AuthenticationForm,
                        'error': 'Username or password is incorrect'
                    })
        else:
            login(request, user)
            return redirect('index')

    else:
        return render(request, 'registration/signin.html', {
            'form':AuthenticationForm
        })
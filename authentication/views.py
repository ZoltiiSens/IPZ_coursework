from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'authentication/home.html')


def signup_user(request):
    if request.method == 'GET':
        context = {'form': UserCreationForm()}
        return render(request, 'authentication/signup.html', context)
    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('week_list')
            except IntegrityError:
                context = {'form': UserCreationForm(), 'error': 'Username has already been taken. Choose the other one'}
                return render(request, 'authentication/signup.html', context)
        else:
            context = {'form': UserCreationForm(), 'error': 'Passwords did not match'}
            return render(request, 'authentication/signup.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {'form': AuthenticationForm()}
        return render(request, 'authentication/login.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('week_list')
        else:
            context = {'form': AuthenticationForm(), 'error': 'Password or username is wrong'}
            return render(request, 'authentication/login.html', context)


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
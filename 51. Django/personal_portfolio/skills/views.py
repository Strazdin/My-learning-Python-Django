from django.shortcuts import render, redirect
from .models import Skills
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'skills/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'skills/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует! Попробуйте другое'})
        else:
            return render(request, 'skills/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпали!'})
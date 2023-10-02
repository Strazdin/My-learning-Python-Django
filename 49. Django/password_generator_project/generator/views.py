from django.shortcuts import render
# from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    length = list(range(6, 25))
    return render(request, 'home.html', {'lst': length})


def password(request):
    chars = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        chars.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        chars.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('special'):
        chars.extend([chr(i) for i in range(33, 48)])

    length = int(request.GET.get('length'))
    psw = ''.join(random.choices(chars, k=length))
    return render(request, 'password.html', {'password': psw})

def about(request):
    return render(request, 'about.html')


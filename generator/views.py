from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    vPassword=''
    length=int(request.GET.get('length',12))
    characters=list('abcdefghijlmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
       characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
       characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
       characters.extend(list('0123456789'))

    for i in range(length):
        vPassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':vPassword})

def about(request):
    return render(request,'generator/about.html')
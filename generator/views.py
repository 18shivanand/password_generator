from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    char = list('asdfghjklzxcvbnmqwertyuiop')
    if request.GET.get('uppercase'):
        char.extend(list('ASFGDHJKLZXCVBNMQWERTYUIOP'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()_+|:><?/'))

    if request.GET.get('number'):
        char.extend(list('1234567890'))

    len=int(request.GET.get('length'))
    thepassword = ''
    for i in range(len):
        thepassword += random.choice(char)

    return render(request,'generator/password.html',{'password':thepassword})

from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'hello/home.html')

def password(request):
    thepassword = ''
    charac = list('abcdefghijklmnopqrsuvwxyz')
    length = int(request.GET.get('length','3'))
    if request.GET.get('uppercase'):
        charac.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        charac.extend(list('0123456789'))
    if request.GET.get('special'):
        charac.extend(list('!@#$%^&*'))
    for x in range(length):
        thepassword+=random.choice(charac)
    return render(request,'hello/password.html',{'password':thepassword})

def about(request):
    return render(request,'hello/about.html')

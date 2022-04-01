from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def recruiterlogin(request):
    return render(request,'recruiterlogin.html')
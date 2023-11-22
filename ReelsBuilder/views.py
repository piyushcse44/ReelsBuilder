from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def pricing(request):
    return render(request,'pricing.html')
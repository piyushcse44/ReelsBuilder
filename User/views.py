from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')


def reset_password(request):
    return render(request,'reset_password.html')

@login_required(login_url='login')
def user_profile(request):
   
    return render(request,'profile.html')


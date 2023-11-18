from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')




def signup(request):
    return render(request,'signup.html')


def reset_password(request):
    return render(request,'reset_password.html')
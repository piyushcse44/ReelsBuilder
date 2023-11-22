from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .form import UserCreationForm
from .models import UserInfo,Videos


# Create your views here.

def custom_login(request):
   
    if request.user.is_authenticated:
        return render(request,'profile.html')
    
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
       
        try:
            user = User.objects.get(username=username)           
        except:
             return render(request, 'login.html', {'error_message': 'User is Not registered'})
        
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'profile.html')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')


def signup(request):

    if request.user.is_authenticated:
        return render(request,'profile.html')
    
    if request.method == 'POST':
        username = request.POST.get('mail')
        password = request.POST.get('password')
        email = username
      
        try :
           user =  User.objects.create(
                username = username,
                password = password,
                email = email
                )
        except :
                return render(request,'signup.html',{"error_message":"Invalid username or password"})
        
        UserInfo.objects.create(
            user = user,
            user_email = user.email,
            video_count=0,
            subscription_status = 'free'
       
        )
        login(request, user)
        return render(request,'login.html')
    
    return render(request, 'signup.html')



def reset_password(request):
    return render(request,'reset_password.html')


@login_required(login_url='login')
def user_profile(request):

    user = request.user
    try :
        user_info = UserInfo.objects.get(user = user)
    except UserInfo.DoesNotExist:
        UserInfo.objects.create(
            user = user,
            user_email = user.email,
            video_count=0,
            subscription_status = 'free'
       
        )
        user_info = UserInfo.objects.get(user = user)


 
    return render(request,'profile.html',{"user_info":user_info})


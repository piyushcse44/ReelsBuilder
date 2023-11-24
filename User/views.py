from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserInfo,GeneraterVideImage


# Create your views here.


def custom_login(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")

    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("pass")
        print(username,password)

        try:
            user = User.objects.get(username=username)
        except:
            return render(
                request, "login.html", {"error_message": "User is Not registered"}
            )

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            return redirect('profile')
        else:
            return render(
                request, "login.html", {"error_message": "Invalid credentials"}
            )

    return render(request, "login.html")



@login_required(login_url="login")
def user_profile(request):
    user = request.user
    try:
        user_info = UserInfo.objects.get(user=user)
    except UserInfo.DoesNotExist:
        UserInfo.objects.create(
            user=user, user_email=user.email , subscription_status="free"
        )
        user_info = UserInfo.objects.get(user=user)
        
   
    video_count = len(user_info.user_video.all())

    
    return render(request, "profile.html", {"user_info": user_info , "video_count": video_count})




def video_generator(request):

    active = ""
    queryobj = GeneraterVideImage.objects.filter(status ="active")

    if queryobj.exists():
        active = queryobj[0].generater_video_image

        
    current_image = {
        "active" : active ,
    }    
    return render(request,"video_generator.html",current_image)

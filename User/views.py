from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .form import CustomUserCreationForm
from .models import UserInfo


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


def signup(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            return redirect("profile")
        else:
            return render(
                request,
                "signup.html",
                {"error_message": "Invalid credentials", "form": form},
            )

    return render(request, "signup.html", {"form": form})


def reset_password(request):
    return render(request, "reset_password.html")


@login_required(login_url="login")
def user_profile(request):
    user = request.user
    try:
        user_info = UserInfo.objects.get(user=user)
    except UserInfo.DoesNotExist:
        UserInfo.objects.create(
            user=user, user_email=user.email, video_count=0, subscription_status="free"
        )
        user_info = UserInfo.objects.get(user=user)

    return render(request, "profile.html", {"user_info": user_info})


def video_generator(request):
    return render(request,"video_generator.html")

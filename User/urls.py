from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import  custom_login,signup,reset_password,user_profile,video_generator



urlpatterns = [
    
    path('login/', custom_login, name="login"),
    path('signup/',signup,name="signup"),
    path('reset_password/',reset_password,name="reset_password"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('profile/',user_profile,name="profile"),
    path('video_generator/',video_generator,name="video_generator"),
    
]

from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import  login,signup,reset_password,user_profile



urlpatterns = [
    
    path('login/', login, name="login"),
    path('signup/',signup,name="signup"),
    path('reset_password/',reset_password,name="reset_password"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('profile/',user_profile,name="profile"),
    
]

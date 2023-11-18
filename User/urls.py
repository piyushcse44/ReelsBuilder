from django.urls import path,include
from .views import login,signup,reset_password

urlpatterns = [

    path('login/',login,name="login"),
    path('signup/',signup,name="signup"),
    path('reset_password/',reset_password,name="reset_password"),
   
]
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

   path('signup/',view_signup_user)
   path('login/',view_login_user,name="login"),
   path('page/',view_restrict_page),
   path('logout/',view_logout_user),
   
]
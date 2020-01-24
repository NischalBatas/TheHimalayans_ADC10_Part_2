from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def view_signup_user(request):
    if request.method =="GET":
        return render(request,'registration/signup.html')
    else:
        print(request.POST)
        user= User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse ("Signup Successful!!")





from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def view_signup_user(request):
    if request.method =="GET":
        return render(request,'registration/signup.html')
    else:
        print(request.POST)
        user= User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Signup Successful!!")

def view_login_user(request):
    if request.method == "GET":
        return render(request,'registration/login.html')
    else:
        user =authenticate(username = request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is None:
            return HttpResponse("Not found")
        else:
            login(request,user)
            return HttpResponse("Successful")

def view_restrict_page(request):
    print(request.user)
    if request.user.is_authenticated:
        return render(request,'restrict.html')
    else:
        return HttpResponse("Not login")


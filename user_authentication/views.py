from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from products.models import Product

# Create your views here.


def view_signup_user(request):
    if request.method =="GET":
        return render(request,'registration/signup.html')
    else:
        print(request.POST)
        user= User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()

    #user permission
    content_type = ContentType.objects.get_for_model(Product)

    #add permission
    permission = Permission.objects.get(
        codename='add_product',
        content_type=content_type,
    )
    user.user_permissions.add(permission)



    #remove permission
    permission = Permission.objects.get(
        codename='delete_product',
        content_type=content_type,
    )
    user.user_permissions.add(permission)
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

def view_logout_user(request):
    logout(request)
    
    return redirect('login')



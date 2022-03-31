from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User


# Create your views here.
def login1(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def signup(request):
    name=request.POST['uname']
    password=request.POST['psw']
    user=auth.authenticate(username=name,password=password)
    if user is not None:
        auth.login(request,user)
    
        return redirect('/')
        
    else:
        return render(request,'login.html',{'emsg':'Invalid !!'})

def logout(request):
    auth.logout(request)
    return redirect('/')

def regin(request):
    firstname=request.POST['fname']
    lastname=request.POST['lname']
    username=request.POST['user']
    Email=request.POST['email']
    Password=request.POST['pswf']
    Re_password=request.POST['psws']

    if Password==Re_password:
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'emsg':'username is already taken'})
        elif User.objects.filter(email=Email).exists():
            return render(request,'register.html',{'emsg':'Email is already taken'})

        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=Email,password=Password)
            user.save();
            print('user created')
            auth.login(request,user)
            return redirect('/')
    else:
        return render(request,'register.html',{'emsg':'password is not match'})


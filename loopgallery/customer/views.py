from django.shortcuts import render,redirect
from django.contrib.auth.models import auth


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
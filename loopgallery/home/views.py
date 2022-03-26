from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def page2(request):
    ln='php'
    return render(request,'page2.html',{'lang':ln})


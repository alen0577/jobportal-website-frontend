from django.shortcuts import render

# Create your views here.

def loginhome(request):
    return render(request,'loginhome.html')

def index(request):
    return render(request,'index.html')
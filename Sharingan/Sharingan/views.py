from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'Sharingan/index.html')
def about(request):
    return render(request,'Sharingan/about.html')

def contact(request):
    return render(request,'Sharingan/contact.html')

def errorpage(request):
    return render(request,'Sharingan/Error.html')
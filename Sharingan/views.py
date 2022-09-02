from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
import socket


def index(request):
    return render(request,'Sharingan/index.html')
def about(request):
    return render(request,'Sharingan/about.html')

def contact(request):
    return render(request,'Sharingan/Challenge.html')

def logs(request):
    return render(request,'logs.txt')
    
def handler_not_found(request, exception,):
    context = {}
    response = render(request, "Sharingan/Error.html", context=context)
    response.status_code = 404
    return response
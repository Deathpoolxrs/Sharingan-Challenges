from sys import flags
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'XSS/index.html')


def xssone(request):
    if request.method == 'GET' and 'p' in request.GET:
        param = request.GET['p']
        if 'alert' in param or 'prompt' in param or 'print' in param:
            flags = 'flag{dafdfdsf}'
            return render(request,'XSS/index.html',{'param':param,'flags':flags})
        else:
            return render(request,'XSS/index.html',{'param':param})
    else:
        return render(request,'XSS/index.html')


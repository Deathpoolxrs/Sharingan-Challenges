from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'XSS/index.html')


def xssone(request):
    if request.method == 'GET' and 'p' in request.GET:
        param = request.GET['p']
        return render(request,'XSS/index.html',{'param':param})
    else:
        return render(request,'XSS/index.html')


from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request,'SSRF/index.html')

def ssrfone(request):
    if request.method == 'GET' and 's' in request.GET:
        param = request.GET['s']
        try:
            r= requests.get(param)
            return render(request,'SSRF/result.html',{'param':r})
        except:
            return render(request,'SSRF/index.html',{'error':'Something Went Wrong'})
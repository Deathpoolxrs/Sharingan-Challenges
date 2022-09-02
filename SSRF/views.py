from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request,'SSRF/index.html')

def ssrfone(request):
    if request.method == 'GET' and 's' in request.GET:
        param = request.GET['s']
        if 'localhost' in param or '127.0.0.1' in param or '0.0.0.0' in param or 'file' in param:
            return render(request,'SSRF/result.html',{'meme':'Filters are everywhere :('})
        else:
            try:
                r= requests.get(param)
                print("Request Internal:"+param)
                return render(request,'SSRF/result.html',{'param':r})
            except:
                return render(request,'SSRF/index.html',{'error':'Invalid URL(Add http/https)/ Unreacheable'})
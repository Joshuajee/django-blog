from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return render(req, "blog/index.html")

def lastest(req):
    return HttpResponse("Working Fine")

def top(req):
    return HttpResponse("Working Fine")
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def  home(request):
    return render(request, "pages/home.html",{})

def courses(request):
    return render(request, "pages/courses.html",{})
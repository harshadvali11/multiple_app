from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def string1(request):
    return HttpResponse('<h1>This is String1 function of app1</h1>')


def string2(request):
    return HttpResponse('<h1>This is String2 function of app1</h1>')
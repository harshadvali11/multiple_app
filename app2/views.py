from django.shortcuts import render

# Create your views here.

def htmlfile1(request):
    return render(request,'htmlfile1.html')


def htmlfile2(request):
    return render(request,'htmlfile2.html')
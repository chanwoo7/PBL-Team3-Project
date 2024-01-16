from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")

def main(request):
    return render(request,'adApp/main.html')

def adManager(request):
    return render(request, 'adApp/adManager.html')
from django.shortcuts import render
from .models import Ad

# Create your views here.
from django.http import HttpResponse

from django.core.paginator import Paginator


def index(request):
    return HttpResponse("Hello World!")

def main(request):
    return render(request,'adApp/main.html')

def adManager(request):
    return render(request, 'adApp/adManager.html')
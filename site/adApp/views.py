from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")


def main(request):
    return render(request, 'adApp/main.html')


def ad_manager(request):
    return render(request, 'adApp/adManager.html')

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
    page = request.GET.get('page', '1')  # 페이지

    ad_list = ["현대","삼성","노동부","피망","코드스테이츠", "1", "2"]

    paginator = Paginator(ad_list, 5)
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'adApp/adManager.html', context)

def ad_list(request):
    return render(request, 'adApp/ad_list.html')
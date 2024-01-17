from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index,name='print'),
    path('main/', views.main, name='main'),
    path('adManager/', views.adManager, name='manager'),
]
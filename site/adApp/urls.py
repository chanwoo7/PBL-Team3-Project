from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='print'),
    path('main/', views.main, name='main'),
    path('adManager/', views.adManager, name='manager')
]

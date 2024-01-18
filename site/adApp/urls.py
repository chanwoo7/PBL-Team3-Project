from django.urls import path
from .api_views import *
from . import views

urlpatterns = [
    # Ad API Endpoints
    path('api/get_ad_details/<int:ad_id>/', AdAPIView.as_view(), name='get_ad_details'),
    path('api/add_ad/', AdAPIView.as_view(), name='add_ad'),
    path('api/edit_ad/<int:ad_id>/', AdAPIView.as_view(), name='edit_ad'),
    path('api/delete_ad/<int:ad_id>/', AdAPIView.as_view(), name='delete_ad'),
    path('api/search_ads/', SearchAdsAPIView.as_view(), name='search_ads'),
    path('api/get_all_ads/', AllAdsAPIView.as_view(), name='get_all_ads'),

    # Media API Endpoints
    path('api/upload_media/', MediaAPIView.as_view(), name='upload_media'),
    path('api/get_media_details/<int:media_id>', MediaAPIView.as_view(), name='get_media_details'),
    path('media/<int:media_id>/', ShowMediaAPIView.as_view(), name='show_media'),

    # HTML 경로
    path('', views.index,name='print'),
    path('main/', views.main, name='main'),
    path('adManager/', views.ad_manager, name='manager'),
]

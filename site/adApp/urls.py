from django.urls import path
from . import api_views

from . import views

urlpatterns = [
    # API 경로
    path('api/add_ad/', api_views.add_ad, name='add_ad'),
    path('api/edit_ad/<int:ad_id>/', api_views.edit_ad, name='edit_ad'),
    path('api/delete_ad/<int:ad_id>/', api_views.delete_ad, name='delete_ad'),
    path('api/search_ads/', api_views.search_ads, name='search_ads'),
    path('api/get_ad_details/<int:ad_id>/', api_views.get_ad_details, name='get_ad_details'),
    path('api/upload_media', api_views.upload_media, name='upload_media'),

    # 광고 이미지/동영상 경로
    path('media/<int:media_id>', api_views.show_media, name='show_media'),

    # HTML 경로
    path('', views.index,name='print'),
    path('main/', views.main, name='main'),
    path('adManager/', views.ad_manager, name='manager'),
]

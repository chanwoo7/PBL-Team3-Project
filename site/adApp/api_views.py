from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ad, Media
from .serializers import AdSerializer, MediaSerializer
from django.db.models import Q


# 광고 생성
@api_view(['POST'])
def add_ad(request):
    if request.method == 'POST':
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 광고 수정
@api_view(['PUT'])
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)

    if request.method == 'PUT':
        serializer = AdSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 광고 삭제
@api_view(['DELETE'])
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)

    if request.method == 'DELETE':
        ad.delete()
        return Response({'message': 'Ad successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)


# 광고 검색
@api_view(['GET'])
def search_ads(request):
    search_type = request.GET.get('search_type', '')
    search_query = request.GET.get('search_query', '')

    # 유효한 search_types 정의
    valid_search_types = ['id', 'adv_id', 'name', 'type', 'text']

    if search_type not in valid_search_types:
        return Response({'error': 'Invalid search_type'}, status=status.HTTP_400_BAD_REQUEST)

    ads = Ad.objects.all()

    if search_query == '':
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)

    # search_type에 따라 필터링
    if search_type == 'id':
        ads = ads.filter(id=search_query)
    elif search_type == 'adv_id':
        ads = ads.filter(advId=search_query)
    elif search_type == 'name':
        ads = ads.filter(name__icontains=search_query)
    elif search_type == 'type':
        ads = ads.filter(type__icontains=search_query)
    elif search_type == 'text':
        ads = ads.filter(text__icontains=search_query)

    # Serialize the queryset
    serializer = AdSerializer(ads, many=True)
    return Response(serializer.data)


# 전체 광고 보기
@api_view(['GET'])
def get_all_ads(request):
    ads = Ad.objects.all()

    serializer = AdSerializer(ads, many=True)
    return Response(serializer.data)


# 광고 상세 보기
@api_view(['GET'])
def get_ad_details(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)

    serializer = AdSerializer(ad)
    return Response(serializer.data)


# 미디어 업로드
@api_view(['POST'])
def upload_media(request):
    if request.method == 'POST':
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 미디어 재생
@api_view(['GET'])
def show_media(request, media_id):
    media = get_object_or_404(Media, pk=media_id)
    file_path = media.file.path
    return FileResponse(open(file_path, 'rb'))


# 미디어 상세 보기
@api_view(['GET'])
def get_media_details(request, media_id):
    media = get_object_or_404(Media, pk=media_id)
    serializer = MediaSerializer(media)
    return Response(serializer.data)

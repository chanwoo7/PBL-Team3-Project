from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ad, MediaTest
from .serializers import AdSerializer, MediaTestSerializer
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
    # Get parameters from the query string
    ad_type = request.GET.get('ad_type', '')
    search_query = request.GET.get('search_query', '')

    # Filter ads based on search criteria
    ads = Ad.objects.filter(
        Q(type__icontains=ad_type) | Q(name__icontains=search_query)
    )

    # Serialize the queryset
    serializer = AdSerializer(ads, many=True)

    return Response(serializer.data)


# 광고 상세 보기
@api_view(['GET'])
def get_ad_details(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)

    serializer = AdSerializer(ad)
    return Response(serializer.data)


# 광고 파일 업로드
@api_view(['POST'])
def upload_media(request):
    if request.method == 'POST':
        serializer = MediaTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 광고 파일 띄우기
@api_view(['GET'])
def show_media(request, media_id):
    media = get_object_or_404(MediaTest, pk=media_id)
    file_path = media.file.path
    return FileResponse(open(file_path, 'rb'))
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ad, Media
from .serializers import AdSerializer, MediaSerializer


class AdAPIView(APIView):
    # get_ad_details
    def get(self, request, ad_id):
        ad = get_object_or_404(Ad, pk=ad_id)
        serializer = AdSerializer(ad)
        return Response(serializer.data)

    # add_ad
    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # edit_ad
    def put(self, request, ad_id):
        ad = get_object_or_404(Ad, pk=ad_id)
        serializer = AdSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete_ad
    def delete(self, request, ad_id):
        ad = get_object_or_404(Ad, pk=ad_id)
        ad.delete()
        return Response({'message': 'Ad successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)


class SearchAdsAPIView(APIView):
    # search_ads
    def get(self, request):
        search_type = request.GET.get('search_type', '')
        search_query = request.GET.get('search_query', '')

        # 유효한 search_types 정의
        valid_search_types = ['id', 'adv_name', 'name', 'type', 'text']

        if search_type not in valid_search_types:
            return Response({'error': 'Invalid search_type'}, status=status.HTTP_400_BAD_REQUEST)

        ads = Ad.objects.all()

        if search_query == '':
            serializer = AdSerializer(ads, many=True)
            return Response(serializer.data)

        # search_type에 따라 필터링
        if search_type == 'id':
            ads = ads.filter(id=search_query)
        elif search_type == 'adv_name':
            ads = ads.filter(adv_name__icontains=search_query)
        elif search_type == 'name':
            ads = ads.filter(name__icontains=search_query)
        elif search_type == 'type':
            ads = ads.filter(type__icontains=search_query)
        elif search_type == 'text':
            ads = ads.filter(text__icontains=search_query)

        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)


class AllAdsAPIView(APIView):
    # get_all_ads
    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)


class MediaAPIView(APIView):
    # get_media_details
    def get(self, request, media_id):
        media = get_object_or_404(Media, pk=media_id)
        serializer = MediaSerializer(media)
        return Response(serializer.data)

    # upload_media
    def post(self, request):
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowMediaAPIView(APIView):
    # show_media
    def get(self, request, media_id):
        media = get_object_or_404(Media, pk=media_id)
        file_path = media.file.path
        return FileResponse(open(file_path, 'rb'))

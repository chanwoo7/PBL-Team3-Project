from rest_framework.serializers import ModelSerializer
from .models import *


class AdvSerializer(ModelSerializer):
    class Meta:
        model = Adv
        fields = '__all__'


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class MediaTestSerializer(ModelSerializer):
    class Meta:
        model = MediaTest
        fields = '__all__'


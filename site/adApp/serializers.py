from rest_framework.serializers import ModelSerializer
from .models import Adv, Ad


class AdvSerializer(ModelSerializer):
    class Meta:
        model = Adv
        fields = '__all__'


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

    advId = AdvSerializer()

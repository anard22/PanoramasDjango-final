from rest_framework import serializers
from core.models import Panorama


class PanoramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panorama
        fields = '__all__'
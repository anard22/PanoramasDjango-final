from rest_framework import serializers
from core.models import Panorama

class PanoramaSerializer(serializers.ModelSerializer):
    creador = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Panorama
        fields = [
            'id',
            'titulo',
            'descripcion',
            'fecha',
            'lugar',
            'creador',
        ]
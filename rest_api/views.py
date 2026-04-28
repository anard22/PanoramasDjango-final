from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.models import Panorama
from .serializers import PanoramaSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def panoramas_api(request):
    """
    GET  -> Lista todos los panoramas
    POST -> Crea un nuevo panorama
    """

    if request.method == 'GET':
        panoramas = Panorama.objects.all()
        serializer = PanoramaSerializer(panoramas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PanoramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creador=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

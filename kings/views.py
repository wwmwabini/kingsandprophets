from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from kings.models import King
from kings.serializers import KingSerializer

@api_view(['GET'])
def get_all_kings(request):
    kings = King.objects.all()
    serializer = KingSerializer(kings, many=True)

    context = {
        "kings": serializer.data
    }

    return Response(context)

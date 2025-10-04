from rest_framework import viewsets
from rest_framework.response import Response

from prophets.models import Prophet
from prophets.serializers import ProphetSerializer

class ProphetViewSet(viewsets.ModelViewSet):
    queryset = Prophet.objects.all()
    serializer_class = ProphetSerializer

    def create(self, request, *args, **kwargs):
        
        
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=201, headers=headers)

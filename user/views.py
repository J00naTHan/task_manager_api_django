from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CommonUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CommonUserSerializer

    @action(detail=False, methods=['get'], url_path='get_by_username/(?P<username>[^/.]+)')
    def get_by_username(self, request, username=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

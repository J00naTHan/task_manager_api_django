from rest_framework import viewsets
from .models import Task
from .serializers import CommonTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = CommonTaskSerializer

from rest_framework import serializers
from .models import Task


class CommonTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'prioridade', 'nome', 'descricao', 'autor', 'envolvidos', 'grupo', 'status', 'dataLimite']

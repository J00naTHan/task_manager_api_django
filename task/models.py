from django.contrib.auth.models import User, Group
from django.db import models


class Task(models.Model):
    ATIVA = "ATV"
    REALIZADA = "RLZ"
    CANCELADA = "CNC"
    STATUS_CHOICES = {
        ATIVA: "Em andamento",
        REALIZADA: "Realizada",
        CANCELADA: "Cancelada",
    }

    class Meta:
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    prioridade = models.SmallIntegerField(default=1)
    nome = models.CharField(max_length=64, default='tarefa sem nome')
    descricao = models.CharField(verbose_name='desrição',  max_length=256, blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    envolvidos = models.ManyToManyField(User, related_name='envolvidos', blank=True, null=True)
    grupo = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=STATUS_CHOICES, max_length=24, default=ATIVA)
    criadaEm = models.DateTimeField(auto_now_add=True)
    atualizadaEm = models.DateTimeField(auto_now=True)
    dataLimite = models.DateTimeField()

    def __str__(self):
        return self.nome + " (" + str(self.id) + ")"

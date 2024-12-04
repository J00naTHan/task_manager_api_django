# Generated by Django 5.1.3 on 2024-12-04 08:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridade', models.SmallIntegerField(default=1)),
                ('nome', models.CharField(default='tarefa sem nome', max_length=64)),
                ('descricao', models.CharField(blank=True, max_length=256, null=True, verbose_name='desrição')),
                ('status', models.CharField(choices=[('ATV', 'Em andamento'), ('RLZ', 'Realizada'), ('CNC', 'Cancelada')], default='ATV', max_length=24)),
                ('criadaEm', models.DateTimeField(auto_now_add=True)),
                ('atualizadaEm', models.DateTimeField(auto_now=True)),
                ('dataLimite', models.DateTimeField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('envolvidos', models.ManyToManyField(blank=True, null=True, related_name='envolvidos', to=settings.AUTH_USER_MODEL)),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
            ],
            options={
                'verbose_name': 'tarefa',
                'verbose_name_plural': 'tarefas',
            },
        ),
    ]

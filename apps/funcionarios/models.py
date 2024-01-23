from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.db.models import Sum


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def total_hora_extra(self):
        total = self.registrohoraextra_set.all().aggregate(Sum('horas'))['horas__sum']
        return total or 0

    def __str__(self):
        return self.nome

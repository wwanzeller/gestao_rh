from django.db import models
from apps.funcionarios.models import Funcionario
from django.shortcuts import reverse

class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Insira o tipo de documento')
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos/', help_text='arquivo do documento')

    def __str__(self):
        return self.descricao

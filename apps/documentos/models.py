from django.db import models

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Insira o tipo de documento')

    def __str__(self):
        return self.descricao

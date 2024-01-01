from django.views.generic import ListView
from .models import Departamento
from apps.funcionarios.models import Funcionario


class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)

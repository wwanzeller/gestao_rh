from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView, CreateView
)
from apps.registro_hora_extra.models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']

    def get_success_url(self):
        return reverse_lazy('horaextra_update', args=[self.object.id])


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('horaextra_list')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas', 'funcionario']
    success_url = reverse_lazy('horaextra_list')

    def get_form(self):
        form = super().get_form()
        form.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=self.request.user.funcionario.empresa
        )
        return form

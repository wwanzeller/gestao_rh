from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Empresa
from django.http import HttpResponse
from django.contrib import messages


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        empresa = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = empresa
        funcionario.save()
        return HttpResponse('ok')


class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nome']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Empresa atualizada com sucesso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro ao atualizar a empresa.")
        return super().form_invalid(form)

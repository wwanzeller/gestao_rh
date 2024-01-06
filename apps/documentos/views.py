from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Documento
from apps.funcionarios.models import Funcionario

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def funcionario_id(self):
        return self.kwargs.get('funcionario_id')

    def form_valid(self, form):
        documento = form.save(commit=False)
        documento.pertence = get_object_or_404(Funcionario, pk=self.funcionario_id())
        documento.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('funcionario_update', kwargs={'pk': self.funcionario_id()})
